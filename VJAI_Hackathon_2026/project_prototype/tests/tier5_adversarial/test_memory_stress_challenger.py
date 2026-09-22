"""
Adversarial Stress Testing Suite: Short-Term SQLite Checkpointer & ChromaDB Vector Store.
Milestone 2 Challenger 2: Memory Persistence & Concurrency Stress.
Focus:
1. SQLite checkpointer multi-threading concurrency (file-based & in-memory).
2. SQLite state recovery, transaction rollbacks, corrupt state, thread isolation.
3. ChromaDB vector store empty collection querying & fallback behavior.
4. ChromaDB diverse queries (empty, unicode, injection, boundaries, k=0).
5. ChromaDB collision detection in add_episodic_reflection & concurrent writes.
"""

import os
import sys
import json
import time
import shutil
import threading
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from core.memory.short_term import ShortTermMemory
from core.memory.vector_store import LongTermVectorMemory, DEFAULT_DOMAIN_DOCUMENTS


class TestSQLiteCheckpointerStress:
    """Stress tests for SQLite ShortTermMemory checkpointer."""

    def test_concurrent_writes_file_based(self, tmp_path):
        """Test concurrent writes across multiple threads to file-based SQLite."""
        db_path = str(tmp_path / "concurrent_test.db")
        memory = ShortTermMemory(db_path=db_path)

        num_threads = 20
        writes_per_thread = 25
        errors = []
        checkpoint_ids = []

        def worker(thread_idx: int):
            for step in range(writes_per_thread):
                t_id = f"thread_{thread_idx}"
                state = {
                    "task_id": f"task_{thread_idx}_{step}",
                    "current_step": step,
                    "worker": thread_idx,
                    "data": f"payload_{thread_idx}_{step}"
                }
                try:
                    cid = memory.save_checkpoint(t_id, state, step=step)
                    checkpoint_ids.append(cid)
                except Exception as e:
                    errors.append((thread_idx, step, type(e).__name__, str(e)))

        threads = [threading.Thread(target=worker, args=(i,)) for i in range(num_threads)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        print(f"\n[File-based SQLite] Completed writes: {len(checkpoint_ids)}, Errors: {len(errors)}")
        if errors:
            print(f"Sample error: {errors[0]}")

        # Verify integrity
        for thread_idx in range(num_threads):
            t_id = f"thread_{thread_idx}"
            history = memory.get_checkpoint_history(t_id)
            # Check if all writes succeeded
            expected_count = writes_per_thread - sum(1 for e in errors if e[0] == thread_idx)
            assert len(history) == expected_count, f"History mismatch for {t_id}: got {len(history)}, expected {expected_count}"

        assert len(errors) == 0, f"Encountered {len(errors)} errors during concurrent file-based writes: {errors[:3]}"

    def test_concurrent_writes_in_memory(self):
        """Test concurrent writes to in-memory SQLite checkpointer."""
        memory = ShortTermMemory(db_path=":memory:")

        num_threads = 10
        writes_per_thread = 20
        errors = []
        checkpoint_ids = []

        def worker(thread_idx: int):
            for step in range(writes_per_thread):
                t_id = f"mem_thread_{thread_idx}"
                state = {
                    "task_id": f"mem_task_{thread_idx}_{step}",
                    "step": step,
                    "thread": thread_idx
                }
                try:
                    cid = memory.save_checkpoint(t_id, state, step=step)
                    checkpoint_ids.append(cid)
                except Exception as e:
                    errors.append((thread_idx, step, type(e).__name__, str(e)))

        threads = [threading.Thread(target=worker, args=(i,)) for i in range(num_threads)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        print(f"\n[In-memory SQLite] Completed writes: {len(checkpoint_ids)}, Errors: {len(errors)}")
        if errors:
            print(f"Sample in-memory error: {errors[0]}")
        assert len(errors) == 0, f"Encountered {len(errors)} errors during concurrent in-memory writes: {errors[:3]}"

    def test_concurrent_read_write_interleaved(self, tmp_path):
        """Test concurrent read and write operations on the same threads."""
        db_path = str(tmp_path / "read_write_interleaved.db")
        memory = ShortTermMemory(db_path=db_path)

        num_threads = 15
        ops_per_thread = 20
        errors = []

        def read_write_worker(thread_idx: int):
            t_id = f"rw_thread_{thread_idx}"
            for step in range(ops_per_thread):
                try:
                    # Write
                    state = {"counter": step, "thread": thread_idx}
                    memory.save_checkpoint(t_id, state, step=step)
                    # Read back immediately
                    latest = memory.get_latest_checkpoint(t_id)
                    assert latest is not None
                    assert latest["step"] >= step
                    # Read history
                    hist = memory.get_checkpoint_history(t_id)
                    assert len(hist) >= 1
                except Exception as e:
                    errors.append((thread_idx, step, type(e).__name__, str(e)))

        threads = [threading.Thread(target=read_write_worker, args=(i,)) for i in range(num_threads)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        print(f"\n[Read/Write Interleaved] Errors: {len(errors)}")
        if errors:
            print(f"Sample error: {errors[0]}")
        assert len(errors) == 0, f"Encountered {len(errors)} errors during interleaved reads/writes: {errors[:3]}"

    def test_state_persistence_and_recovery_after_reopen(self, tmp_path):
        """Test full state recovery when reopening database across instances."""
        db_path = str(tmp_path / "persistence_recovery.db")

        # Session 1: write diverse complex state
        mem1 = ShortTermMemory(db_path=db_path)
        complex_state = {
            "task_id": "recovery_task_001",
            "scenario_id": "an_giang_rice_001",
            "irrigation": {"water_needed_mm": 24.5, "valve_open": True},
            "floats": [0.123456789, -45.67, 1e-5],
            "unicode_text": "Nông nghiệp tái sinh 日本語テスト 🌾 28.1%",
            "nested": {"level1": {"level2": {"level3": [1, 2, 3, None, True, False]}}}
        }
        cid1 = mem1.save_checkpoint("thread_persist", complex_state, step=1)
        cid2 = mem1.save_checkpoint("thread_persist", {"step": 2, "status": "completed"}, step=2)

        # Force dereference of mem1
        del mem1

        # Session 2: reopen same database file with fresh instance
        mem2 = ShortTermMemory(db_path=db_path)
        latest = mem2.get_latest_checkpoint("thread_persist")
        assert latest is not None
        assert latest["step"] == 2
        assert latest["state"]["status"] == "completed"

        history = mem2.get_checkpoint_history("thread_persist")
        assert len(history) == 2
        assert history[0]["step"] == 1
        assert history[0]["state"]["unicode_text"] == "Nông nghiệp tái sinh 日本語テスト 🌾 28.1%"
        assert history[0]["state"]["nested"]["level1"]["level2"]["level3"] == [1, 2, 3, None, True, False]
        assert history[1]["step"] == 2

    def test_clear_thread_isolation(self, tmp_path):
        """Test that clear_thread only purges the target thread and leaves others intact."""
        db_path = str(tmp_path / "clear_isolation.db")
        mem = ShortTermMemory(db_path=db_path)

        mem.save_checkpoint("thread_A", {"data": "A1"}, step=1)
        mem.save_checkpoint("thread_A", {"data": "A2"}, step=2)
        mem.save_checkpoint("thread_B", {"data": "B1"}, step=1)

        mem.clear_thread("thread_A")
        assert mem.get_latest_checkpoint("thread_A") is None
        assert len(mem.get_checkpoint_history("thread_A")) == 0

        # thread_B must remain untouched
        b_latest = mem.get_latest_checkpoint("thread_B")
        assert b_latest is not None
        assert b_latest["state"]["data"] == "B1"

    def test_sanitize_state_handles_non_serializable_objects(self, tmp_path):
        """Test _sanitize_state properly converts custom objects without crashing."""
        db_path = str(tmp_path / "sanitize_test.db")
        mem = ShortTermMemory(db_path=db_path)

        class CustomObj:
            def __str__(self):
                return "CustomObjRepresented"

        class DictObj:
            def dict(self):
                return {"val": 999}

        class ModelDumpObj:
            def model_dump(self, mode=None):
                return {"pydantic_field": "validated"}

        problematic_state = {
            "custom": CustomObj(),
            "dict_obj": DictObj(),
            "model_obj": ModelDumpObj(),
            "path": Path("/dummy/path"),
        }

        cid = mem.save_checkpoint("thread_sanitize", problematic_state, step=1)
        assert cid.startswith("thread_sanitize_1_")
        loaded = mem.get_latest_checkpoint("thread_sanitize")
        assert loaded["state"]["custom"] == "CustomObjRepresented"
        assert loaded["state"]["dict_obj"] == {"val": 999}
        assert loaded["state"]["model_obj"] == {"pydantic_field": "validated"}

    def test_langgraph_sqlite_saver_cross_thread_programming_error(self, tmp_path):
        """Test that get_langgraph_checkpointer(use_sqlite=True) fails when accessed across threads."""
        db_path = str(tmp_path / "langgraph_thread.db")
        mem = ShortTermMemory(db_path=db_path)
        cp = mem.get_langgraph_checkpointer(use_sqlite=True)

        thread_errors = []
        def worker():
            try:
                list(cp.list({"configurable": {"thread_id": "test_th"}}))
            except Exception as e:
                thread_errors.append((type(e).__name__, str(e)))

        t = threading.Thread(target=worker)
        t.start()
        t.join()

        # Verification of thread safety: no ProgrammingError occurs
        assert len(thread_errors) == 0, f"Expected 0 cross-thread errors on synchronized SqliteSaver, got: {thread_errors}"


class TestChromaDBVectorStoreStress:
    """Stress tests for ChromaDB LongTermVectorMemory."""

    def test_empty_collection_querying(self, tmp_path):
        """Test behavior when querying an empty collection."""
        persist_dir = str(tmp_path / "chroma_empty_test")
        vmem = LongTermVectorMemory(persist_directory=persist_dir)

        # Episodic memory is empty initially
        if vmem._episodic_col:
            count = vmem._episodic_col.count()
            print(f"\n[Empty Collection] Episodic collection initial count: {count}")
            assert count == 0

        # Query episodic memory
        res = vmem.search_episodic_memory("irrigation scheduling reflection", k=2)
        print(f"[Empty Collection] search_episodic_memory returned: {res}")
        # Investigate what it returned: did it return empty list or fallback domain doc?
        assert isinstance(res, list)

    def test_empty_episodic_collection_leaks_domain_fallback(self, tmp_path):
        """Empirically demonstrates semantic leaking: empty episodic query returns domain documents."""
        persist_dir = str(tmp_path / "chroma_leak_test")
        vmem = LongTermVectorMemory(persist_directory=persist_dir)

        # Querying an empty episodic memory collection should return [] without domain leakage
        res = vmem.search_episodic_memory("irrigation scheduling reflection", k=2)
        assert res == [], f"Expected empty list from empty episodic collection, got: {res}"


    def test_episodic_reflection_duplicate_id_collision(self, tmp_path):
        """Test adding multiple episodic reflections with same task_id and length."""
        persist_dir = str(tmp_path / "chroma_collision_test")
        vmem = LongTermVectorMemory(persist_directory=persist_dir)

        # Both reflections have length 14:
        ref1 = "Reflection AAA"  # len 14
        ref2 = "Reflection BBB"  # len 14

        task_id = "task_collision_01"
        vmem.add_episodic_reflection(task_id, "scenario_1", ref1, "SUCCESS")
        # Second reflection with same task_id and same len(reflection)
        vmem.add_episodic_reflection(task_id, "scenario_2", ref2, "FAILURE")

        # Check episodic collection count
        if vmem._episodic_col:
            count = vmem._episodic_col.count()
            print(f"\n[Collision Test] Episodic count after 2 additions: {count}")
            # Did the second one get added, or was it silently dropped?
            res = vmem._episodic_col.get()
            print(f"[Collision Test] Stored IDs: {res.get('ids')}")
            assert count == 2, f"Collision caused silent drop: stored IDs={res.get('ids')}"

    def test_diverse_queries_and_boundaries(self, tmp_path):
        """Test vector store with diverse edge-case queries."""
        persist_dir = str(tmp_path / "chroma_diverse_test")
        vmem = LongTermVectorMemory(persist_directory=persist_dir)

        test_queries = [
            "",  # empty string
            "   \t\n  ",  # whitespace
            "🌾 日本語テスト 農業の二酸化炭素排出削減 ST25 gạo lúa nước",  # Multilingual UTF-8
            "A" * 5000,  # very long string
            "'; DROP TABLE agent_checkpoints; --",  # SQL injection syntax
            r".*+?^${}()|[]\\",  # regex specials
            "<script>alert('xss')</script>",  # script tags
            "FAO-56 AWD 38% reduction N2O GWP 265",  # exact technical terms
        ]

        for q in test_queries:
            try:
                results = vmem.similarity_search(q, k=3)
                assert isinstance(results, list)
                assert len(results) >= 1
                for r in results:
                    assert "document" in r
                    assert "metadata" in r
                    assert "score" in r
                    assert 0.0 <= r["score"] <= 1.0
            except Exception as e:
                pytest.fail(f"Query failed on '{q[:30]}': {type(e).__name__}: {str(e)}")

    def test_k_boundary_values(self, tmp_path):
        """Test k boundary values: k=0, k=1, k=100 (exceeding collection size)."""
        persist_dir = str(tmp_path / "chroma_k_test")
        vmem = LongTermVectorMemory(persist_directory=persist_dir)

        # k = 0
        try:
            res_k0 = vmem.similarity_search("rice irrigation", k=0)
            print(f"\n[k=0 Test] Returned: {len(res_k0)} results")
        except Exception as e:
            print(f"\n[k=0 Test] Raised exception: {type(e).__name__}: {e}")

        # k = 1
        res_k1 = vmem.similarity_search("rice irrigation", k=1)
        assert len(res_k1) == 1

        # k = 100 (more than documents in collection)
        res_k100 = vmem.similarity_search("rice irrigation", k=100)
        assert len(res_k100) <= len(DEFAULT_DOMAIN_DOCUMENTS)
        assert len(res_k100) > 0

    def test_concurrent_vector_searches(self, tmp_path):
        """Test concurrent similarity searches from multiple threads."""
        persist_dir = str(tmp_path / "chroma_concurrent_test")
        vmem = LongTermVectorMemory(persist_directory=persist_dir)

        num_threads = 15
        queries_per_thread = 10
        errors = []

        queries = [
            "AWD water management",
            "IPCC fertilizer emission factor",
            "EVN peak electricity tariff",
            "Scope 2 grid emission factor Vietnam",
            "MAFF Japan GX compliance"
        ]

        def search_worker(thread_idx: int):
            for i in range(queries_per_thread):
                q = queries[(thread_idx + i) % len(queries)]
                try:
                    res = vmem.similarity_search(q, k=2)
                    assert len(res) >= 1
                except Exception as e:
                    errors.append((thread_idx, i, type(e).__name__, str(e)))

        threads = [threading.Thread(target=search_worker, args=(i,)) for i in range(num_threads)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        print(f"\n[Concurrent Searches] Errors: {len(errors)}")
        assert len(errors) == 0, f"Encountered {len(errors)} errors in concurrent searches: {errors[:3]}"

    def test_concurrent_episodic_writes(self, tmp_path):
        """Test concurrent writes to episodic memory."""
        persist_dir = str(tmp_path / "chroma_episodic_concurrent")
        vmem = LongTermVectorMemory(persist_directory=persist_dir)

        num_threads = 10
        writes_per_thread = 5
        errors = []

        def write_worker(thread_idx: int):
            for i in range(writes_per_thread):
                task_id = f"task_th{thread_idx}_iter{i}"
                reflection = f"Thread {thread_idx} run {i}: optimized water to {20 + i}mm"
                try:
                    vmem.add_episodic_reflection(task_id, "scenario_stress", reflection, "SUCCESS")
                except Exception as e:
                    errors.append((thread_idx, i, type(e).__name__, str(e)))

        threads = [threading.Thread(target=write_worker, args=(i,)) for i in range(num_threads)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        print(f"\n[Concurrent Episodic Writes] Errors: {len(errors)}")
        assert len(errors) == 0, f"Errors during concurrent episodic additions: {errors}"
