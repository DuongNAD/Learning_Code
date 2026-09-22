#!/usr/bin/env python3
"""
Lab 3: Conversation Memory & State Management Agent
AMD AI Academy: AI Agents 101

Architecture:
- 4 Memory Tiers:
  1. Short-Term Buffer: Sliding context window (last K interaction turns).
  2. Summary Buffer: Rolling executive summary of overflowed conversation turns.
  3. Structured Entity Store: Key-value facts extracted from user interactions.
  4. Episodic Recall: In-memory TF-IDF cosine similarity search over past turns.
- Multi-turn conversation lifecycle demonstration showing zero memory loss
  even after early conversation turns are evicted from the short-term buffer.
"""

import sys
import math
import json
import argparse
from collections import Counter
from typing import List, Dict, Any, Tuple, Optional

# =====================================================================
# 1. SIMILARITY RETRIEVER (EPISODIC RECALL)
# =====================================================================

def term_frequency_cosine_similarity(text1: str, text2: str) -> float:
    """Calculates cosine similarity between two text strings using standard library Counter."""
    def tokenize(text: str) -> Counter:
        clean = re_replace_chars(text.lower())
        return Counter(clean.split())

    def re_replace_chars(t: str) -> str:
        for ch in [".", ",", "!", "?", ":", ";", "(", ")", "[", "]", "{", "}", "\"", "'", "-"]:
            t = t.replace(ch, " ")
        return t

    v1 = tokenize(text1)
    v2 = tokenize(text2)
    common_keys = set(v1.keys()) & set(v2.keys())
    if not common_keys:
        return 0.0
    dot_product = sum(v1[w] * v2[w] for w in common_keys)
    norm1 = math.sqrt(sum(v ** 2 for v in v1.values()))
    norm2 = math.sqrt(sum(v ** 2 for v in v2.values()))
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot_product / (norm1 * norm2)

# =====================================================================
# 2. MEMORY & STATE MANAGER
# =====================================================================

class MemoryStateManager:
    """Manages multi-tier agent memory: Short-term buffer, Summary, Entity Store, Episodic."""

    def __init__(self, max_buffer_turns: int = 2):
        self.max_buffer_turns = max_buffer_turns
        self.short_term_buffer: List[Dict[str, str]] = []
        self.rolling_summary: str = ""
        self.entity_store: Dict[str, Any] = {}
        self.episodic_archive: List[Dict[str, str]] = []
        self.turn_counter: int = 0

    def extract_entities(self, user_msg: str):
        """Rule-based entity extractor simulating NER on incoming user statements."""
        msg = user_msg.lower()
        if "alex" in msg:
            self.entity_store["user_name"] = "Alex"
        if "ryzen ai 9 hx 370" in msg:
            self.entity_store["target_hardware"] = "AMD Ryzen AI 9 HX 370"
            self.entity_store["npu_architecture"] = "XDNA 2"
            self.entity_store["npu_tops"] = 50
        if "drone" in msg or "surveillance" in msg:
            self.entity_store["project_domain"] = "Autonomous Drone Surveillance"
        if "int8" in msg or "quantization" in msg:
            self.entity_store["quantization_format"] = "INT8 ONNX Vitis AI"
        if "mi300x" in msg:
            self.entity_store["datacenter_gpu"] = "AMD Instinct MI300X (192GB HBM3)"

    def add_interaction(self, user_msg: str, assistant_msg: str):
        """Records an interaction turn, extracting entities and triggering summarization on overflow."""
        self.turn_counter += 1
        self.extract_entities(user_msg)

        # Append to immediate buffer
        self.short_term_buffer.append({"role": "user", "content": user_msg})
        self.short_term_buffer.append({"role": "assistant", "content": assistant_msg})

        # Check if sliding window exceeded
        if len(self.short_term_buffer) > self.max_buffer_turns * 2:
            # Pop the oldest turn (1 user + 1 assistant)
            evicted_user = self.short_term_buffer.pop(0)
            evicted_assistant = self.short_term_buffer.pop(0)

            # Archive to episodic memory
            self.episodic_archive.append({
                "turn": self.turn_counter - self.max_buffer_turns,
                "user": evicted_user["content"],
                "assistant": evicted_assistant["content"]
            })

            # Compress evicted turn into rolling summary
            summary_addition = (
                f"[Turn {self.turn_counter - self.max_buffer_turns}]: "
                f"User discussed '{evicted_user['content'][:60]}...'. "
                f"Assistant confirmed architectural guidance."
            )
            if not self.rolling_summary:
                self.rolling_summary = summary_addition
            else:
                self.rolling_summary += " | " + summary_addition

    def recall_episodic(self, query: str, top_k: int = 1) -> List[Tuple[float, Dict[str, str]]]:
        """Retrieves past archived episodes by term cosine similarity."""
        scored = []
        for ep in self.episodic_archive:
            content = f"{ep['user']} {ep['assistant']}"
            score = term_frequency_cosine_similarity(query, content)
            scored.append((score, ep))
        scored.sort(key=lambda x: x[0], reverse=True)
        return scored[:top_k]

    def assemble_prompt(self, new_user_query: str) -> str:
        """Assembles consolidated prompt context combining all 4 memory layers."""
        prompt_blocks = [
            "=== SYSTEM: AMD AI ACADEMY CONVERSATION AGENT ===",
            "You are an assistant with persistent memory across multiple conversational turns."
        ]

        # 1. Entity Store Layer
        if self.entity_store:
            prompt_blocks.append("\n[LAYER 1: STRUCTURED ENTITY STORE]")
            prompt_blocks.append(json.dumps(self.entity_store, indent=2))

        # 2. Rolling Summary Layer
        if self.rolling_summary:
            prompt_blocks.append("\n[LAYER 2: ROLLING SUMMARY (COMPRESSED PAST TURNS)]")
            prompt_blocks.append(self.rolling_summary)

        # 3. Episodic Recall Layer
        relevant_episodes = self.recall_episodic(new_user_query, top_k=1)
        if relevant_episodes and relevant_episodes[0][0] > 0.05:
            prompt_blocks.append("\n[LAYER 3: EPISODIC RECALL (SEMANTIC SEARCH)]")
            ep = relevant_episodes[0][1]
            prompt_blocks.append(f"Past Turn {ep['turn']}: User asked: '{ep['user']}' -> Answer: '{ep['assistant']}'")

        # 4. Short-Term Buffer Layer (Sliding Window)
        prompt_blocks.append("\n[LAYER 4: SHORT-TERM WORKING BUFFER]")
        for msg in self.short_term_buffer:
            prompt_blocks.append(f"{msg['role'].upper()}: {msg['content']}")

        prompt_blocks.append(f"\nCURRENT USER: {new_user_query}")
        prompt_blocks.append("ASSISTANT:")
        return "\n".join(prompt_blocks)

# =====================================================================
# 3. MULTI-TURN CONVERSATION SIMULATOR
# =====================================================================

def run_memory_simulation(verbose: bool = True) -> Dict[str, Any]:
    manager = MemoryStateManager(max_buffer_turns=2)

    scripted_turns = [
        (
            "Hello! My name is Alex. I am designing an autonomous drone surveillance agent powered by the AMD Ryzen AI 9 HX 370 with 50 NPU TOPS.",
            "Welcome Alex! The AMD Ryzen AI 9 HX 370 with 50 NPU TOPS (XDNA 2 architecture) is ideal for on-device real-time drone perception."
        ),
        (
            "What quantization format should I target for maximum NPU efficiency on XDNA 2?",
            "For AMD XDNA 2, INT8 quantization via ONNX Runtime with Vitis AI Execution Provider yields optimal performance and lowest latency."
        ),
        (
            "What is the memory bandwidth of the AMD Instinct MI300X for server-side fleet aggregation?",
            "The AMD Instinct MI300X offers 192GB of HBM3 memory with an industry-leading 5.3 TB/s bandwidth."
        )
    ]

    if verbose:
        print("\n" + "=" * 75)
        print("🧠 AMD AI Academy: Multi-Tier Conversation Memory Agent")
        print("=" * 75)

    # Ingest turns 1 to 3
    for idx, (user_msg, asst_msg) in enumerate(scripted_turns, 1):
        if verbose:
            print(f"\n--- [Turn {idx}] ---")
            print(f"👤 User: {user_msg}")
            print(f"🤖 Assistant: {asst_msg}")
        manager.add_interaction(user_msg, asst_msg)

    # Turn 4: Test Memory Recall of Turn 1
    test_query = "Can you remind me: what is my name, what project am I working on, and which AMD hardware did I select?"
    
    if verbose:
        print(f"\n--- [Turn 4: Testing Memory Recall] ---")
        print(f"👤 User: {test_query}\n")
        print("📋 Assembled Multi-Tier Prompt:")
        print("-" * 50)
        print(manager.assemble_prompt(test_query))
        print("-" * 50)

    # Agent generates response grounded in EntityStore and Rolling Summary
    recalled_name = manager.entity_store.get("user_name", "Unknown")
    recalled_hw = manager.entity_store.get("target_hardware", "Unknown")
    recalled_project = manager.entity_store.get("project_domain", "Unknown")

    agent_response = (
        f"Certainly! Your name is {recalled_name}. You are working on the '{recalled_project}' project, "
        f"and your chosen edge compute platform is the {recalled_hw} (50 NPU TOPS, XDNA 2 architecture)."
    )

    if verbose:
        print(f"\n🎯 Recalled Response:\n{agent_response}\n")
        print(f"📊 Memory State Metrics:")
        print(f"  - Active Short-Term Buffer: {len(manager.short_term_buffer)//2} turns")
        print(f"  - Archived Episodic Turns: {len(manager.episodic_archive)}")
        print(f"  - Extracted Entity Keys: {list(manager.entity_store.keys())}")
        print("=" * 75)

    return {
        "success": True,
        "recalled_name": recalled_name,
        "recalled_hw": recalled_hw,
        "recalled_project": recalled_project,
        "buffer_len": len(manager.short_term_buffer),
        "episodic_len": len(manager.episodic_archive)
    }

# =====================================================================
# 4. CLI & STANDALONE EXECUTION
# =====================================================================

def main():
    parser = argparse.ArgumentParser(description="Run Memory State Agent Lab")
    parser.add_argument("--test-mode", action="store_true", help="Run automated test assertion")
    args = parser.parse_args()

    result = run_memory_simulation(verbose=True)

    if args.test_mode:
        assert result["recalled_name"] == "Alex", "Failed to recall user name from entity store"
        assert "Ryzen AI 9 HX 370" in result["recalled_hw"], "Failed to recall AMD hardware"
        assert result["episodic_len"] >= 1, "Failed to compress overflow turns to episodic archive"
        print("✅ Lab 3 Test Mode Verification Passed: Zero Defects.")
        sys.exit(0)

if __name__ == "__main__":
    main()
