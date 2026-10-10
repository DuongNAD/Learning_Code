# TEST_INFRA.md — Automated Test Infrastructure & Verification Architecture

Course: GCI World 2026 September · Matsuo-Iwasawa Laboratory (The University of Tokyo)  
System: ThreeUI Explorable Interactive Learning System & Slide Engine  
Test Architecture Version: 2.1.0  
Compliance: Strict RFC 2119, `emoji_policy: none` (Zero Unicode Emojis)  
Last Updated: 2026-09-24T18:50:00Z  

---

## 1. Test Philosophy & Methodological Framework

The test infrastructure for the ThreeUI Explorable Interactive Learning System is grounded in an opaque-box, requirement-driven, mathematically rigorous verification philosophy. The suite validates that all interactive learning modules, state engines, mathematical formulas, and presentation surfaces strictly satisfy their pedagogical specifications and runtime performance invariants without altering or degrading legacy coursework assets.

The testing methodology employs a **4-Tier Systematic Approach**:

```
+-----------------------------------------------------------------------------+
|                     4-Tier Systematic Verification Framework                |
+-----------------------------------------------------------------------------+
| Tier A: Category-Partition Testing                                          |
| - Equivalence partitioning across input domains (Weather: Rain/Normal/Sun)  |
| - Operational stances (Conservative alpha=0, Aggressive alpha=1)            |
| - View modes (Explorable Document vs 16:9 Presentation Slide Deck)          |
+-----------------------------------------------------------------------------+
| Tier B: Boundary Value Analysis (BVA)                                       |
| - Inventory extremes (Q = 0, Q = D, Q >> D, Stockout at t_open vs t_close)  |
| - Dimension bounds (N = 10^2 to 10^7, Strides with step=1, 2, 3)            |
| - Broadcasting limits (Trailing dim = 1 vs matching vs mismatch)            |
+-----------------------------------------------------------------------------+
| Tier C: Pairwise & Combinatorial Testing                                    |
| - Matrix shape compatibility: (3,1)+(1,4)->(3,4); (4,3)+(3,)->(4,3)        |
| - Theme states (Dark / Light) combined with View states (Doc / Deck)        |
| - Mathematical cost trade-offs (Cu vs Co, Salvage value vs Scrap loss)      |
+-----------------------------------------------------------------------------+
| Tier D: Real-World Workload & Latency Invariants                            |
| - Sub-16ms reactive frame budget (< 16.6ms / 60fps)                         |
| - Zero Cumulative Layout Shift (CLS = 0) with in-place KaTeX .dyn-slot DOM   |
| - file:// USB portability without CORS or module import failures            |
+-----------------------------------------------------------------------------+
```

---

## 2. Feature Inventory & Test Mapping (F38 – F55)

The following matrix formally maps every Phase 2 feature (F38 through F55) to its automated test case, acceptance invariant, and verification method:

| Feature ID | Feature Name | Test Class & Method | Test Tier | Acceptance Criteria / Invariant Verified |
| :--- | :--- | :--- | :--- | :--- |
| **F38** | ThreeUI Design System Spec | `TestTier1CoreEngineAndDesignSystem.test_css_design_system_tokens` | Tier 1 | Verifies CSS custom properties (`--bg-primary`, `--accent-cyan`, `--glass-blur`), Inter & JetBrains Mono font declarations, and dual-theme palettes. |
| **F39** | Tri-Layer Glassmorphism & WebGL BG | `TestTier1CoreEngineAndDesignSystem.test_glassmorphism_and_webgl_bg` | Tier 1 | Verifies `backdrop-filter: blur(16px)`, `@supports` fallback rules, and standalone WebGL shader canvas configuration without heavy runtime libraries. |
| **F40** | Reactive State Flow DAG Engine | `TestTier1CoreEngineAndDesignSystem.test_reactive_signal_store_contract` | Tier 1 | Inspects `createStore` implementation in JS: verifies `requestAnimationFrame` batching, dirty-key propagation, and listener notification invariants. |
| **F41** | KaTeX In-Place Slot Optimization | `TestTier1CoreEngineAndDesignSystem.test_katex_in_place_slot_architecture` | Tier 1 | Verifies `.dyn-slot` containment classes, `contain: layout style`, `font-variant-numeric: tabular-nums`, and zero Cumulative Layout Shift (CLS = 0). |
| **F42** | Dual-View Unified Controller | `TestTier1CoreEngineAndDesignSystem.test_dual_view_unified_controller_contract` | Tier 1 | Verifies `data-view="document"` vs `data-view="deck"`, 16:9 auto-scaler rules, keyboard event handlers (`ArrowRight`, `Space`, `V`), and persistent store state across views. |
| **F43** | Web-Native UMD/IIFE Portability | `TestTier1CoreEngineAndDesignSystem.test_umd_iife_global_portability` | Tier 1 | Verifies universal IIFE enclosure (`window.ThreeUIEngine`), absence of bare ES module imports, ensuring 100% operation under `file://` USB protocol. |
| **F44** | Buoi 1 Food Truck Dark Data Model | `TestTier2MathematicalContracts.test_food_truck_newsvendor_and_dark_data` | Tier 2 | Verifies Newsvendor critical fractile $F^* = \frac{p-c}{p-s} \approx 64.3\%$, observed sales $\min(Q,D)$, dark data $\max(0, D-Q)$, and stockout time equation. |
| **F45** | Buoi 1 Compound Data Flywheel | `TestTier2MathematicalContracts.test_compound_data_flywheel_dynamics` | Tier 2 | Verifies 5-node cyclic sequence, recurrence formulas $N(k)=N_0(1+\gamma)^k$, $\text{Acc}(k)$, switching cost $C_{\text{switch}}(k)$, and Moat Depth Score $M(k) \in [0\%, 100\%]$. |
| **F46** | Buoi 1 Seven-Eleven Tanpin Kanri | `TestTier2MathematicalContracts.test_tanpin_kanri_loss_tradeoff_balance` | Tier 2 | Verifies 4-phase empirical loop, optimal fractile $\alpha^* = \frac{C_u}{C_u + C_o}$, and opportunity loss vs disposal loss convex trade-off curve. |
| **F47** | Buoi 2 NumPy Slicing & Memory Strides | `TestTier2MathematicalContracts.test_numpy_strides_and_affine_address_mapping` | Tier 2 | Verifies C-contiguous stride recursion, 2D/3D affine byte address mapping $\text{Addr}(i,j) = \text{Base} + i \cdot S_0 + j \cdot S_1$, and View vs Copy zero-copy invariant. |
| **F48** | Buoi 2 NumPy Broadcasting Visualizer | `TestTier2MathematicalContracts.test_broadcasting_trailing_alignment_and_rules` | Tier 2 | Verifies right-to-left trailing alignment, dimension compatibility ($d_A == d_B$ or $d == 1$), shape derivation $(3,1)+(1,4)\to(3,4)$, and stride-0 virtual projection. |
| **F49** | Buoi 2 Vectorization Speed Simulator | `TestTier2MathematicalContracts.test_vectorization_speedup_analytical_model` | Tier 2 | Verifies analytical timing $T_{\text{py}}(N) \approx 62.5N\text{ ns}$, $T_{\text{np}}(N) \approx 2500 + 0.21N\text{ ns}$, and asymptotic speedup curve $S(N) \approx 100\times - 300\times$. |
| **F50** | Cornell Notebook [Chép vào vở] Blocks | `TestTier3CornellAndBoilerplates.test_cornell_three_column_schema` | Tier 3 | Verifies 3-column Cornell schema (`[Chép vào vở]`: Cues 20-22%, Mindmap/Geometry 43-50%, Invariant/Code 30-35%) across curriculum notes. |
| **F51** | Extensible Boilerplates for Weeks 3+ | `TestTier3CornellAndBoilerplates.test_future_week_boilerplates_spec` | Tier 3 | Verifies boilerplate templates and specs for Pandas (Session 3), ML Loss Landscapes (Session 5-6), and Scaled Dot-Product Attention (Session 8+). |
| **F52** | Explorable Master Hub & Navigator | `TestTier1CoreEngineAndDesignSystem.test_explorable_hub_navigator_contract` | Tier 1 | Verifies structure, session links, demo access, and layout standards of the master explorable hub. |
| **F53** | Dual-Track E2E Test Suite | `TestTier5ZeroRegressionAndSuiteIntegrity.test_test_suite_composition` | Tier 5 | Self-verification: asserts comprehensive coverage across all 5 test tiers within `tests/test_threeui_explorable_engine.py`. |
| **F54** | Universal Zero-Emoji Compliance | `TestTier4WorkspaceZeroEmojiAudit.test_zero_emojis_in_explorable_deliverables` | Tier 4 | Scans all `.html`, `.css`, `.js`, `.md` deliverables in `explorable/` (and workspace) enforcing `emoji_policy: none` using strict Unicode regex. |
| **F55** | Zero Regression Safety | `TestTier5ZeroRegressionAndSuiteIntegrity.test_legacy_test_suite_preservation` | Tier 5 | Verifies that all 180 legacy tests across 6 existing test files in `tests/` remain 100% intact, unmodified, and fully operational. |

---

## 3. Test Architecture & Execution Semantics

### 3.1 Directory Layout
```
GCI_World_2026_September/
├── TEST_INFRA.md                          # Test Architecture & Feature Mapping (This Document)
├── explorable/                            # Dedicated Explorable Engine Workspace
│   ├── index.html                         # Explorable Master Hub
│   ├── engine/
│   │   ├── threeui-engine.js              # Core Reactive Signal Store & View Controller
│   │   ├── threeui-engine.css             # Glassmorphism & Theme Stylesheet
│   │   └── threeui-shader-bg.js           # Vanilla WebGL Ambient Background Shader
│   ├── buoi1/
│   │   ├── index.html                     # Buoi 1 Dual-View Explorable Document & Deck
│   │   └── models_buoi1.js                # Buoi 1 Interactive Mathematical Models
│   ├── buoi2/
│   │   ├── index.html                     # Buoi 2 Dual-View Explorable Document & Deck
│   │   └── models_buoi2.js                # Buoi 2 Interactive Mathematical Models
│   └── templates/
│       └── boilerplate_explorable.html    # Extensible Boilerplate for Weeks 3+
└── tests/
    ├── test_threeui_explorable_engine.py  # Dual-Track E2E Test Suite (Tiers 1 to 5)
    ├── test_curriculum_matrix_and_policy.py (21 legacy tests)
    ├── test_empirical_challenger.py       (32 legacy tests)
    ├── test_micro_practice_roadmap_challenger.py (16 legacy tests)
    ├── test_milestone3_roadmap_and_guide.py (21 legacy tests)
    ├── test_study_notes.py                (18 legacy tests)
    └── test_syllabus_and_slides.py        (72 legacy tests)
```

### 3.2 Progressive Testability Semantics

In adherence to progressive testability guidelines:
1. **Unconditional Ground-Truth Oracles (Mathematical Tier 2)**:
   All mathematical formulations (Newsvendor fractile, Dark Data censoring, Compound Data Flywheel recurrence, 7-Eleven loss trade-off, NumPy memory strides, broadcasting trailing rules, and SIMD speedup equations) are evaluated unconditionally against algorithmic Python reference implementations. These tests run immediately and verify system truth independent of file creation milestones.
2. **Graceful Artifact-Bound Verification (Tiers 1, 3, 4)**:
   For physical deliverables that are generated progressively across milestones (`explorable/engine/`, `explorable/buoi1/`, `explorable/buoi2/`, `explorable/templates/`):
   - If an artifact is not yet present on disk, tests report a clean skipped notification (`[SKIP] Artifact pending implementation`).
   - As soon as worker agents write an artifact, the test harness automatically transitions from skipped to active inspection, strictly validating file presence, non-emptiness, UTF-8 encoding, syntactic validity, CSS containment rules, and zero-emoji compliance.
   - This ensures the test suite exhibits **zero false failures** during intermediate milestone handoffs, while enforcing complete adversarial rigor upon artifact landing.

---

## 4. Test Execution Commands & Pass/Fail Criteria

### 4.1 Test Runner Commands

- **Full Project Discovery (Legacy + New E2E Suite):**
  ```bash
  python3 -m unittest discover tests
  ```
- **Targeted ThreeUI Explorable Engine Test Suite:**
  ```bash
  python3 -m unittest tests/test_threeui_explorable_engine.py
  ```
- **Verbose Output with Individual Test Names:**
  ```bash
  python3 -m unittest -v tests/test_threeui_explorable_engine.py
  ```

### 4.2 Pass/Fail Criteria (RFC 2119)

1. The test suite MUST exit with return code `0`.
2. Failures (`F`) and Errors (`E`) MUST equal `0`.
3. Skipped tests (`s`) ARE PERMITTED ONLY for physical artifacts belonging to milestones not yet authored.
4. Total execution time of the entire test suite (180 legacy tests + new tests) MUST remain under 3.0 seconds on standard development hardware.
5. All deliverables in `explorable/` MUST contain exactly zero unicode emojis matching the standard Unicode regex scanner.

---
*End of TEST_INFRA.md.*
