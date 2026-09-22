# Remediation Specification: Memory Concurrency & Vector Store (M2-2)

**Author**: Milestone 2 Remediation Explorer 2  
**Date**: 2026-09-08  
**Status**: APPROVED_SPECIFICATION  
**Scope**: `core/memory/short_term.py`, `core/memory/vector_store.py`, and `tests/tier5_adversarial/test_memory_stress_challenger.py`

---

## 1. Executive Summary & Root Cause Analysis

Adversarial stress testing conducted by Challenger M2-2 uncovered four distinct defects in the Dual-Tier Memory Layer under multi-threaded concurrency and edge-case query conditions:

| # | Defect | Root Cause | Impact |
|---|--------|------------|--------|
| **1** | In-Memory SQLite race condition (`52/200` errors) | `ShortTermMemory(":memory:")` shares a single `sqlite3.Connection` across threads with `check_same_thread=False` but without a mutex (`threading.RLock`). Concurrent threads corrupt SQLite's C-level parser/connection state. | `DatabaseError: no more rows available`, `InterfaceError: bad parameter or other API misuse`. |
| **2** | File-based SQLite write lock contention (`4/500` errors) | File-based connections use SQLite's default rollback journal (`journal_mode=DELETE`) and default 5.0s timeout. Concurrent write bursts block the entire database file beyond 5s. | `OperationalError: database is locked`. |
| **3** | LangGraph `SqliteSaver` thread affinity crash | `_get_connection()` creates file connections with `check_same_thread=True`. When passed to `SqliteSaver`, background threads cannot execute queries. | `ProgrammingError: SQLite objects created in a thread can only be used in that same thread`. |
| **4** | ChromaDB episodic memory duplicate ID collision & silent loss | Document IDs are constructed as `f"ep_{task_id}_{len(reflection)}"`. Two reflections of identical length for the same task collide on ID; `add()` rejects duplicates and `except Exception: pass` swallows the error. | Second reflection is silently and permanently lost. |
| **5** | ChromaDB empty collection crash & semantic leakage | Querying an empty collection calls `n_results=min(k, max(col.count(), 1))=1`, which crashes ChromaDB. The crash triggers `_lexical_search_fallback`, which returns FAO-56 domain documents for episodic reflection queries. | Agent episodic reflection queries on clean deployments return agronomic rules instead of `[]`. |

---

## 2. Remediation Architecture

```
                                      +-----------------------------------+
                                      |         ShortTermMemory           |
                                      +-----------------------------------+
                                                        |
                            +---------------------------+---------------------------+
                            |                                                       |
               In-Memory Mode (":memory:")                             File-Based Mode ("data/checkpoints.db")
                            |                                                       |
         [threading.RLock() synchronized]                               [threading.RLock() + WAL Mode]
        Single shared connection handle:                               - timeout = 30.0s
        check_same_thread = False                                      - check_same_thread = False
        Guards all SELECT / INSERT / DELETE                            - PRAGMA journal_mode = WAL;
                                                                       - PRAGMA busy_timeout = 30000;
                                                                       - PRAGMA synchronous = NORMAL;

                                      +-----------------------------------+
                                      |       LongTermVectorMemory        |
                                      +-----------------------------------+
                                                        |
                            +---------------------------+---------------------------+
                            |                                                       |
                 Episodic Memory Collection                              Domain Knowledge Collection
                            |                                                       |
        - ID: ep_{task_id}_{timestamp_ms}_{uuid8}                      - Seed standard agronomic / carbon docs
        - .upsert() instead of .add()                                  - Guard col.count() == 0
        - If col.count() == 0 -> return []                             - Guard k <= 0 -> return []
        - Fallback: collection != domain -> return []                  - Lexical fallback isolated to domain docs
```

---

## 3. Detailed Specification: `core/memory/short_term.py`

### 3.1 Concrete Changes
1. **Thread Synchronization Mutex**:
   - Add `import threading`.
   - In `__init__`: initialize `self._lock = threading.RLock()`.
   - Wrap all database executions in `_init_sqlite_db()`, `save_checkpoint()`, `get_latest_checkpoint()`, `get_checkpoint_history()`, `clear_thread()`, and `get_langgraph_checkpointer()` inside `with self._lock:`.
2. **Connection Parameters**:
   - In `_get_connection()`: for file-based SQLite, instantiate with `timeout=30.0` and `check_same_thread=False`:
     ```python
     conn = sqlite3.connect(self.db_path, timeout=30.0, check_same_thread=False)
     conn.execute("PRAGMA busy_timeout = 30000;")
     return conn
     ```
3. **Database Initialization PRAGMAs**:
   - In `_init_sqlite_db()`: when `not self._is_in_memory`:
     ```python
     cursor.execute("PRAGMA journal_mode=WAL;")
     cursor.execute("PRAGMA busy_timeout=30000;")
     cursor.execute("PRAGMA synchronous=NORMAL;")
     ```
4. **LangGraph Checkpointer Thread Affinity**:
   - `get_langgraph_checkpointer(use_sqlite=True)` will use `_get_connection()` which now supplies `check_same_thread=False`.

### 3.2 Target Code Snippet (`core/memory/short_term.py`)

```python
import json
import sqlite3
import os
import threading
from pathlib import Path
from typing import Dict, Any, List, Optional
from datetime import datetime, timezone

try:
    from langgraph.checkpoint.sqlite import SqliteSaver
except ImportError:
    SqliteSaver = None

try:
    from langgraph.checkpoint.memory import MemorySaver
except ImportError:
    MemorySaver = None


class ShortTermMemory:
    """
    Manages short-term working memory, state persistence, and LangGraph checkpointers.
    Thread-safe implementation with SQLite WAL mode and re-entrant locking.
    """

    def __init__(self, db_path: str = "data/checkpoints.db"):
        self.db_path = db_path
        self._is_in_memory = (db_path == ":memory:")
        self._shared_conn = None
        self._lock = threading.RLock()

        if not self._is_in_memory:
            os.makedirs(os.path.dirname(db_path) if os.path.dirname(db_path) else ".", exist_ok=True)
        else:
            self._shared_conn = sqlite3.connect(":memory:", check_same_thread=False)

        self._init_sqlite_db()
        self._memory_saver = MemorySaver() if MemorySaver else None
        self._sqlite_saver = None

    def _get_connection(self) -> sqlite3.Connection:
        if self._is_in_memory:
            return self._shared_conn
        conn = sqlite3.connect(self.db_path, timeout=30.0, check_same_thread=False)
        conn.execute("PRAGMA busy_timeout = 30000;")
        return conn

    def _init_sqlite_db(self):
        """Initializes direct SQLite tables for state inspection and auditability."""
        with self._lock:
            conn = self._get_connection()
            try:
                cursor = conn.cursor()
                if not self._is_in_memory:
                    cursor.execute("PRAGMA journal_mode=WAL;")
                    cursor.execute("PRAGMA busy_timeout=30000;")
                    cursor.execute("PRAGMA synchronous=NORMAL;")
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS agent_checkpoints (
                        checkpoint_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        thread_id TEXT NOT NULL,
                        step INTEGER NOT NULL,
                        timestamp TEXT NOT NULL,
                        state_json TEXT NOT NULL
                    )
                """)
                cursor.execute("""
                    CREATE INDEX IF NOT EXISTS idx_thread_step 
                    ON agent_checkpoints (thread_id, step)
                """)
                conn.commit()
            finally:
                if not self._is_in_memory:
                    conn.close()

    def save_checkpoint(self, thread_id: str, state: Dict[str, Any], step: int = 0) -> str:
        """Persists a state dictionary snapshot for the given thread_id."""
        now = datetime.now(timezone.utc).isoformat()
        clean_state = self._sanitize_state(state)
        state_str = json.dumps(clean_state, ensure_ascii=False)

        with self._lock:
            conn = self._get_connection()
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO agent_checkpoints (thread_id, step, timestamp, state_json)
                    VALUES (?, ?, ?, ?)
                """, (thread_id, step, now, state_str))
                checkpoint_id = cursor.lastrowid
                conn.commit()
                return f"{thread_id}_{step}_{checkpoint_id}"
            finally:
                if not self._is_in_memory:
                    conn.close()

    def get_latest_checkpoint(self, thread_id: str) -> Optional[Dict[str, Any]]:
        """Retrieves the most recent checkpoint state for a thread."""
        with self._lock:
            conn = self._get_connection()
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT step, timestamp, state_json 
                    FROM agent_checkpoints 
                    WHERE thread_id = ? 
                    ORDER BY step DESC, checkpoint_id DESC 
                    LIMIT 1
                """, (thread_id,))
                row = cursor.fetchone()
                if not row:
                    return None
                return {
                    "step": row[0],
                    "timestamp": row[1],
                    "state": json.loads(row[2])
                }
            finally:
                if not self._is_in_memory:
                    conn.close()

    def get_checkpoint_history(self, thread_id: str) -> List[Dict[str, Any]]:
        """Returns all checkpoint snapshots for a thread ordered chronologically."""
        with self._lock:
            conn = self._get_connection()
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT step, timestamp, state_json 
                    FROM agent_checkpoints 
                    WHERE thread_id = ? 
                    ORDER BY step ASC, checkpoint_id ASC
                """, (thread_id,))
                rows = cursor.fetchall()
                return [
                    {
                        "step": row[0],
                        "timestamp": row[1],
                        "state": json.loads(row[2])
                    }
                    for row in rows
                ]
            finally:
                if not self._is_in_memory:
                    conn.close()

    def clear_thread(self, thread_id: str) -> None:
        """Removes all checkpoints associated with a thread_id."""
        with self._lock:
            conn = self._get_connection()
            try:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM agent_checkpoints WHERE thread_id = ?", (thread_id,))
                conn.commit()
            finally:
                if not self._is_in_memory:
                    conn.close()

    @staticmethod
    def prune_context(messages: List[Any], max_recent: int = 8) -> List[Any]:
        if len(messages) <= max_recent:
            return messages
        return messages[-max_recent:]

    def get_langgraph_checkpointer(self, use_sqlite: bool = False) -> Any:
        if use_sqlite and SqliteSaver:
            with self._lock:
                if not self._sqlite_saver:
                    conn = self._get_connection()
                    self._sqlite_saver = SqliteSaver(conn)
                return self._sqlite_saver
        if self._memory_saver:
            return self._memory_saver
        return None

    def _sanitize_state(self, state: Dict[str, Any]) -> Dict[str, Any]:
        clean = {}
        for k, v in state.items():
            if isinstance(v, (str, int, float, bool, type(None), list, dict)):
                clean[k] = v
            elif hasattr(v, "model_dump"):
                clean[k] = v.model_dump(mode="json")
            elif hasattr(v, "dict"):
                clean[k] = v.dict()
            else:
                clean[k] = str(v)
        return clean
```

---

## 4. Detailed Specification: `core/memory/vector_store.py`

### 4.1 Concrete Changes
1. **Collision-Free Episodic IDs & Idempotent Upsert**:
   - Add `import uuid` and `import time`.
   - In `add_episodic_reflection`:
     ```python
     timestamp_ms = int(time.time() * 1000)
     unique_suffix = uuid.uuid4().hex[:8]
     entry_id = f"ep_{task_id}_{timestamp_ms}_{unique_suffix}"
     ```
   - Replace `.add(...)` with `.upsert(...)`.
2. **Safe Boundary and Empty Collection Handling**:
   - In `similarity_search`:
     - If `k <= 0`: immediately return `[]`.
     - Check `col.count()` before executing query:
       ```python
       col_count = col.count()
       if col_count == 0:
           if collection_name == "episodic_memory":
               return []
           return self._lexical_search_fallback(query, k, collection_name)
       ```
     - Clamp `actual_k = max(1, min(k, col_count))` to ensure `n_results` is never greater than available elements and never 0.
3. **Lexical Search Fallback Isolation**:
   - In `_lexical_search_fallback`:
     ```python
     if collection_name != "domain_knowledge":
         return []
     ```
     This strictly isolates domain knowledge from leaking into reflections when vector search fails or collections are empty.
   - If `k <= 0`: return `[]`.
4. **Thread Safety**:
   - In `__init__`: initialize `self._lock = threading.RLock()`.
   - Wrap `add_episodic_reflection` and `similarity_search` in `with self._lock:` to ensure clean, serialized operations across worker threads.

### 4.2 Target Code Snippet (`core/memory/vector_store.py`)

```python
import os
import re
import math
import time
import uuid
import threading
from typing import Dict, Any, List, Optional
from pathlib import Path

try:
    import chromadb
    from chromadb.config import Settings
except ImportError:
    chromadb = None

DEFAULT_DOMAIN_DOCUMENTS = [
    # ... existing 9 domain documents ...
]


class LongTermVectorMemory:
    """
    ChromaDB-backed long-term memory store for semantic domain knowledge
    and episodic task reflections.
    """

    def __init__(self, persist_directory: str = "data/chroma_db"):
        self.persist_directory = persist_directory
        self._client = None
        self._domain_col = None
        self._episodic_col = None
        self._lock = threading.RLock()
        self._init_store()

    def _init_store(self):
        """Initializes ChromaDB collections and seeds baseline knowledge."""
        if chromadb:
            try:
                os.makedirs(self.persist_directory, exist_ok=True)
                self._client = chromadb.PersistentClient(path=self.persist_directory)
                self._domain_col = self._client.get_or_create_collection("domain_knowledge")
                self._episodic_col = self._client.get_or_create_collection("episodic_memory")
                
                if self._domain_col.count() == 0:
                    self.seed_default_knowledge()
                return
            except Exception:
                try:
                    self._client = chromadb.Client()
                    self._domain_col = self._client.get_or_create_collection("domain_knowledge")
                    self._episodic_col = self._client.get_or_create_collection("episodic_memory")
                    if self._domain_col.count() == 0:
                        self.seed_default_knowledge()
                    return
                except Exception:
                    self._client = None

        self._client = None

    def seed_default_knowledge(self):
        """Seeds standard domain documents into the knowledge base."""
        if self._domain_col:
            ids = [d["id"] for d in DEFAULT_DOMAIN_DOCUMENTS]
            docs = [d["document"] for d in DEFAULT_DOMAIN_DOCUMENTS]
            metas = [d["metadata"] for d in DEFAULT_DOMAIN_DOCUMENTS]
            try:
                self._domain_col.upsert(ids=ids, documents=docs, metadatas=metas)
            except Exception:
                pass

    def similarity_search(
        self,
        query: str,
        k: int = 3,
        collection_name: str = "domain_knowledge"
    ) -> List[Dict[str, Any]]:
        """
        Executes semantic search against ChromaDB, with zero-dependency keyword/TF-IDF fallback.
        Thread-safe and boundary-checked.
        """
        if k <= 0:
            return []

        with self._lock:
            col = self._domain_col if collection_name == "domain_knowledge" else self._episodic_col
            if col and self._client:
                try:
                    col_count = col.count()
                    if col_count == 0:
                        if collection_name == "episodic_memory":
                            return []
                        return self._lexical_search_fallback(query, k, collection_name)

                    actual_k = max(1, min(k, col_count))
                    res = col.query(query_texts=[query], n_results=actual_k)
                    documents = res.get("documents", [[]])[0]
                    metadatas = res.get("metadatas", [[]])[0]
                    distances = res.get("distances", [[]])[0] if res.get("distances") else [0.0] * len(documents)
                    
                    results = []
                    for i, doc in enumerate(documents):
                        score = round(1.0 / (1.0 + float(distances[i])) if i < len(distances) else 0.85, 3)
                        meta = metadatas[i] if i < len(metadatas) else {}
                        results.append({
                            "document": doc,
                            "metadata": meta,
                            "score": score
                        })
                    if results:
                        return results
                except Exception:
                    pass

            # Fallback deterministic lexical ranker
            return self._lexical_search_fallback(query, k, collection_name)

    def add_episodic_reflection(
        self,
        task_id: str,
        scenario: str,
        reflection: str,
        outcome: str
    ):
        """
        Records an episodic reflection entry from a completed agent run.
        Uses millisecond timestamp and UUID suffix to guarantee uniqueness.
        """
        doc = f"Scenario: {scenario} | Reflection: {reflection} | Outcome: {outcome}"
        meta = {"task_id": task_id, "scenario": scenario, "outcome": outcome}
        
        timestamp_ms = int(time.time() * 1000)
        unique_suffix = uuid.uuid4().hex[:8]
        entry_id = f"ep_{task_id}_{timestamp_ms}_{unique_suffix}"

        with self._lock:
            if self._episodic_col:
                try:
                    self._episodic_col.upsert(ids=[entry_id], documents=[doc], metadatas=[meta])
                    return
                except Exception:
                    pass

    def search_episodic_memory(self, query: str, k: int = 2) -> List[Dict[str, Any]]:
        """Searches past task reflections."""
        return self.similarity_search(query, k=k, collection_name="episodic_memory")

    def _lexical_search_fallback(self, query: str, k: int, collection_name: str) -> List[Dict[str, Any]]:
        """Deterministic term-overlap fallback ranking when vector embeddings are unavailable."""
        if k <= 0:
            return []

        # Episodic memory should never leak domain guidelines
        if collection_name != "domain_knowledge":
            return []

        q_tokens = set(re.findall(r"\w+", query.lower()))
        scored = []
        for item in DEFAULT_DOMAIN_DOCUMENTS:
            doc_tokens = set(re.findall(r"\w+", item["document"].lower()))
            overlap = len(q_tokens & doc_tokens)
            if overlap > 0:
                score = round(min(0.99, 0.5 + 0.1 * overlap), 2)
                scored.append({
                    "document": item["document"],
                    "metadata": item["metadata"],
                    "score": score
                })
        scored.sort(key=lambda x: x["score"], reverse=True)
        return scored[:k] if scored else [{
            "document": DEFAULT_DOMAIN_DOCUMENTS[0]["document"],
            "metadata": DEFAULT_DOMAIN_DOCUMENTS[0]["metadata"],
            "score": 0.75
        }]
```

---

## 5. Test Suite Alignment Specification (`tests/tier5_adversarial/test_memory_stress_challenger.py`)

### 5.1 Test Analysis
Two tests in Challenger M2-2's suite were written specifically as **exploit proof assertions** (i.e. asserting that the bug triggers):
1. `test_langgraph_sqlite_saver_cross_thread_programming_error`:
   - Line 250: `assert len(thread_errors) > 0` and `assert thread_errors[0][0] == "ProgrammingError"`.
   - Once fixed, `thread_errors` is `[]` (no `ProgrammingError` occurs).
   - **Remediation update**: Update assertion to verify thread safety: `assert len(thread_errors) == 0`.
2. `test_empty_episodic_collection_leaks_domain_fallback`:
   - Line 283: `assert len(res) > 0` and `assert "fao" in res[0]["document"].lower()`.
   - Once fixed, `res` is `[]`.
   - **Remediation update**: Update assertion to verify that empty episodic collection returns an empty list without leakage: `assert res == []`.

All other 12 tests in the suite are regression assertions that will pass cleanly with the fixes:
- `test_concurrent_writes_file_based`: Passes (0 errors).
- `test_concurrent_writes_in_memory`: Passes (previously failed with 52 errors).
- `test_concurrent_read_write_interleaved`: Passes (0 errors).
- `test_state_persistence_and_recovery_after_reopen`: Passes (full state recovery).
- `test_clear_thread_isolation`: Passes (thread isolation preserved).
- `test_sanitize_state_handles_non_serializable_objects`: Passes (Pydantic/Path serialized).
- `test_empty_collection_querying`: Passes (`isinstance(res, list)`).
- `test_episodic_reflection_duplicate_id_collision`: Passes (previously failed: `assert 1 == 2`, now `assert count == 2`).
- `test_diverse_queries_and_boundaries`: Passes (multilingual, SQL injection, regex).
- `test_k_boundary_values`: Passes (`k=0`, `k=1`, `k=100`).
- `test_concurrent_vector_searches`: Passes (15 threads concurrent searches).
- `test_concurrent_episodic_writes`: Passes (10 threads concurrent episodic additions).

---

## 6. Verification & Invalidation Protocol

### Verification Commands
```bash
# 1. Verify in-memory SQLite concurrency fix
py -m pytest -v tests/tier5_adversarial/test_memory_stress_challenger.py::TestSQLiteCheckpointerStress::test_concurrent_writes_in_memory

# 2. Verify episodic reflection collision fix
py -m pytest -v tests/tier5_adversarial/test_memory_stress_challenger.py::TestChromaDBVectorStoreStress::test_episodic_reflection_duplicate_id_collision

# 3. Verify baseline Milestone 2 agent test suite remains green
py -m pytest -v tests/test_agent_core_m2.py

# 4. Verify entire stress test suite
py -m pytest -v tests/tier5_adversarial/test_memory_stress_challenger.py
```

### Invalidation Conditions
- Any write errors (`InterfaceError`, `SystemError`, `DatabaseError`, `OperationalError: database is locked`) during concurrent thread executions.
- Any ID collisions in episodic reflections causing counts to deviate from added items.
- Any domain knowledge documents returned when querying empty episodic reflection memory.
- Any regression in baseline tests in `tests/test_agent_core_m2.py`.
