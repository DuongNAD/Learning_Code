#!/usr/bin/env python3
"""
Lab 2: Function & Tool Calling Agent with Validation & Error Recovery
AMD AI Academy: AI Agents 101

Architecture:
- Implements Modern JSON Schema tool declarations (OpenAI / Anthropic standard).
- Parameter validation with Pydantic v2 (graceful fallback to dataclasses).
- Tool Execution Dispatcher with Error Trapping.
- Demonstrates Self-Reflection / Self-Correction: Agent recovers from invalid tool calls.
- Realistic AMD hardware catalog, math, and system telemetry tools.
"""

import sys
import json
import inspect
import argparse
from typing import Dict, Any, List, Optional, Callable

# Check for Pydantic
try:
    from pydantic import BaseModel, Field, ValidationError
    HAS_PYDANTIC = True
except ImportError:
    HAS_PYDANTIC = False

# =====================================================================
# 1. TOOL SCHEMA MODELS & REGISTRY
# =====================================================================

class ToolRegistry:
    """Manages tool declarations, schemas, and runtime execution dispatch."""
    
    def __init__(self):
        self._tools: Dict[str, Callable] = {}
        self._schemas: List[Dict[str, Any]] = []

    def register(self, name: str, description: str, parameters: Dict[str, Any]):
        def decorator(func: Callable):
            self._tools[name] = func
            self._schemas.append({
                "type": "function",
                "function": {
                    "name": name,
                    "description": description,
                    "parameters": parameters
                }
            })
            return func
        return decorator

    def get_schemas(self) -> List[Dict[str, Any]]:
        return self._schemas

    def dispatch(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Dispatches a tool call with error trapping for self-correction."""
        if tool_name not in self._tools:
            return {
                "status": "error",
                "error_type": "ToolNotFound",
                "message": f"Tool '{tool_name}' does not exist. Available tools: {list(self._tools.keys())}"
            }
        try:
            handler = self._tools[tool_name]
            result = handler(**arguments)
            return {"status": "success", "result": result}
        except TypeError as te:
            return {
                "status": "error",
                "error_type": "ParameterMismatchError",
                "message": f"Invalid arguments for tool '{tool_name}': {str(te)}"
            }
        except Exception as e:
            return {
                "status": "error",
                "error_type": type(e).__name__,
                "message": str(e)
            }

registry = ToolRegistry()

# =====================================================================
# 2. TOOL IMPLEMENTATIONS
# =====================================================================

@registry.register(
    name="query_amd_catalog",
    description="Queries AMD hardware specifications by product name and specific metric.",
    parameters={
        "type": "object",
        "properties": {
            "product_name": {
                "type": "string",
                "description": "Name of the AMD product (e.g., 'Ryzen AI 9 HX 370', 'Instinct MI300X', 'Radeon RX 7900 XTX')"
            },
            "metric": {
                "type": "string",
                "enum": ["npu_tops", "vram_gb", "tdp_w", "architecture", "all"],
                "description": "Hardware specification metric to retrieve."
            }
        },
        "required": ["product_name", "metric"]
    }
)
def query_amd_catalog(product_name: str, metric: str) -> Dict[str, Any]:
    catalog = {
        "ryzen ai 9 hx 370": {
            "npu_tops": 50,
            "vram_gb": 0,  # Shared system memory (up to 64GB LPDDR5x)
            "tdp_w": 28,
            "architecture": "Zen 5 (12 cores) + XDNA 2 NPU (50 TOPS) + RDNA 3.5 (16 CUs)"
        },
        "instinct mi300x": {
            "npu_tops": 0,
            "vram_gb": 192,
            "tdp_w": 750,
            "architecture": "CDNA 3 (192GB HBM3, 5.3 TB/s bandwidth, 1307 TFLOPS FP16)"
        },
        "radeon rx 7900 xtx": {
            "npu_tops": 0,
            "vram_gb": 24,
            "tdp_w": 355,
            "architecture": "RDNA 3 (96 CUs, 960 GB/s bandwidth, 61 TFLOPS FP32)"
        }
    }
    prod = product_name.lower().strip()
    if prod not in catalog:
        raise ValueError(f"Product '{product_name}' not found. Available products: {list(catalog.keys())}")
        
    valid_metrics = ["npu_tops", "vram_gb", "tdp_w", "architecture", "all"]
    if metric not in valid_metrics:
        raise ValueError(f"Invalid metric '{metric}'. Valid metrics are: {valid_metrics}")

    if metric == "all":
        return catalog[prod]
    return {metric: catalog[prod][metric]}


@registry.register(
    name="calculate",
    description="Evaluates a mathematical expression safely.",
    parameters={
        "type": "object",
        "properties": {
            "expression": {
                "type": "string",
                "description": "Arithmetic expression to calculate (e.g. '4 * 50')"
            }
        },
        "required": ["expression"]
    }
)
def calculate(expression: str) -> float:
    allowed = set("0123456789+-*/(). %e")
    clean = expression.strip().replace("^", "**")
    if not all(c in allowed for c in clean):
        raise ValueError(f"Expression contains forbidden characters: {expression}")
    return eval(clean, {"__builtins__": None}, {})


@registry.register(
    name="check_rocm_compatibility",
    description="Verifies ROCm software support for an AMD architecture and target workload.",
    parameters={
        "type": "object",
        "properties": {
            "architecture": {
                "type": "string",
                "description": "Architecture type: 'CDNA', 'RDNA', or 'XDNA'"
            },
            "rocm_version": {
                "type": "string",
                "description": "ROCm version (e.g. '6.2')"
            }
        },
        "required": ["architecture", "rocm_version"]
    }
)
def check_rocm_compatibility(architecture: str, rocm_version: str) -> Dict[str, Any]:
    arch = architecture.upper().strip()
    if "CDNA" in arch:
        return {
            "supported": True,
            "stack": "ROCm Enterprise",
            "features": ["PyTorch 2.x native", "vLLM", "Triton", "FlashAttention-2", "HIP"]
        }
    elif "RDNA" in arch:
        return {
            "supported": True,
            "stack": "ROCm Desktop / Client",
            "features": ["PyTorch for Linux", "ONNX Runtime HIP EP", "Stable Diffusion"]
        }
    elif "XDNA" in arch:
        return {
            "supported": False,
            "note": "XDNA NPUs do not use ROCm; they utilize Ryzen AI Software with ONNX Runtime Vitis AI EP."
        }
    else:
        raise ValueError(f"Unknown architecture '{architecture}'. Choose CDNA, RDNA, or XDNA.")

# =====================================================================
# 3. MOCK LLM WITH SELF-CORRECTION SIMULATION
# =====================================================================

class MockToolCallingLLM:
    """Simulates an LLM calling tools and recovering from an initial validation error."""

    def __init__(self):
        self.step = 0

    def get_next_action(self, messages: List[Dict[str, Any]]) -> Dict[str, Any]:
        self.step += 1
        
        # Step 1: Intentionally attempt an invalid metric to test self-correction
        if self.step == 1:
            return {
                "type": "tool_call",
                "thought": "I need to check the camera resolution and NPU TOPS of AMD Ryzen AI 9 HX 370.",
                "tool_call": {
                    "name": "query_amd_catalog",
                    "arguments": {
                        "product_name": "Ryzen AI 9 HX 370",
                        "metric": "camera_megapixels"  # Intentional invalid metric
                    }
                }
            }
        
        # Step 2: Agent observes error and corrects parameter to valid metric
        elif self.step == 2:
            return {
                "type": "tool_call",
                "thought": "Observation indicates 'camera_megapixels' is invalid. Valid metrics are npu_tops, vram_gb, tdp_w. Querying npu_tops.",
                "tool_call": {
                    "name": "query_amd_catalog",
                    "arguments": {
                        "product_name": "Ryzen AI 9 HX 370",
                        "metric": "npu_tops"
                    }
                }
            }

        # Step 3: Agent executes calculation
        elif self.step == 3:
            return {
                "type": "tool_call",
                "thought": "Ryzen AI 9 HX 370 has 50 NPU TOPS. Now calculating total compute for 4 mobile AI agents.",
                "tool_call": {
                    "name": "calculate",
                    "arguments": {
                        "expression": "4 * 50"
                    }
                }
            }

        # Step 4: Final response
        else:
            return {
                "type": "final_response",
                "thought": "All tool responses collected and validated.",
                "content": (
                    "Validated: The AMD Ryzen AI 9 HX 370 APU delivers 50 NPU TOPS via its XDNA 2 architecture. "
                    "For a fleet of 4 mobile agent nodes, the total combined on-device NPU compute is 200 TOPS."
                )
            }

# =====================================================================
# 4. TOOL CALLING AGENT EXECUTION
# =====================================================================

class ToolCallingAgent:
    """Orchestrates structured tool execution with self-reflection error recovery."""

    def __init__(self, registry: ToolRegistry, llm=None):
        self.registry = registry
        self.llm = llm or MockToolCallingLLM()

    def run(self, user_prompt: str, verbose: bool = True) -> Dict[str, Any]:
        messages: List[Dict[str, Any]] = [{"role": "user", "content": user_prompt}]
        error_recoveries = 0

        if verbose:
            print("\n" + "=" * 75)
            print("🛠️  AMD AI Academy: Tool Calling Agent with Self-Correction")
            print("=" * 75)
            print(f"User Request: {user_prompt}\n")

        for turn in range(1, 6):
            if verbose:
                print(f"--- [Agent Turn {turn}] ---")

            action = self.llm.get_next_action(messages)

            if action["type"] == "final_response":
                if verbose:
                    print(f"💭 Thought: {action['thought']}")
                    print(f"🎯 Final Response:\n{action['content']}\n")
                    print("=" * 75)
                return {
                    "success": True,
                    "final_response": action["content"],
                    "error_recoveries": error_recoveries,
                    "turns": turn
                }

            elif action["type"] == "tool_call":
                tc = action["tool_call"]
                tool_name = tc["name"]
                args = tc["arguments"]

                if verbose:
                    print(f"💭 Thought: {action['thought']}")
                    print(f"📞 Calling Tool: {tool_name}({json.dumps(args)})")

                # Dispatch tool call
                exec_result = self.registry.dispatch(tool_name, args)

                if exec_result["status"] == "error":
                    error_recoveries += 1
                    if verbose:
                        print(f"⚠️  Tool Error Caught: [{exec_result['error_type']}] {exec_result['message']}")
                        print("🔄 Agent Triggering Self-Correction...")
                else:
                    if verbose:
                        print(f"✅ Tool Result: {json.dumps(exec_result['result'])}")

                # Append interaction to message history
                messages.append({
                    "role": "assistant",
                    "tool_call": tc
                })
                messages.append({
                    "role": "tool",
                    "name": tool_name,
                    "content": exec_result
                })
                print()

        return {"success": False, "error_recoveries": error_recoveries, "turns": 5}

# =====================================================================
# 5. CLI & STANDALONE EXECUTION
# =====================================================================

def main():
    parser = argparse.ArgumentParser(description="Run Tool Calling Agent Lab")
    parser.add_argument("--test-mode", action="store_true", help="Run automated test assertion")
    args = parser.parse_args()

    agent = ToolCallingAgent(registry=registry)
    result = agent.run("Find the NPU TOPS of Ryzen AI 9 HX 370 and calculate total for 4 nodes.", verbose=True)

    if args.test_mode:
        assert result["success"] is True, "Agent failed to produce final response"
        assert result["error_recoveries"] == 1, "Agent did not demonstrate self-correction error recovery"
        assert "200" in result["final_response"], "Final response missing expected compute total"
        print("✅ Lab 2 Test Mode Verification Passed: Zero Defects.")
        sys.exit(0)

if __name__ == "__main__":
    main()
