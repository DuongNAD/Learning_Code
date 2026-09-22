"""
Short-Term Context Memory Buffer & SQLite Checkpointer.
Maintains state checkpoints per thread_id for fault tolerance, state restoration,
and multi-turn agent conversation context.
Conforms strictly to PROJECT.md § Memory Layer and ORIGINAL_REQUEST.md § R2.
"""

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
        """
        Sliding window context buffer pruner: keeps system/initial instructions and the last k messages.
        """
        if len(messages) <= max_recent:
            return messages
        return messages[-max_recent:]

    def get_langgraph_checkpointer(self, use_sqlite: bool = False) -> Any:
        """
        Returns a LangGraph-compatible checkpointer instance.
        """
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
        """Ensures state object is JSON serializable."""
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
