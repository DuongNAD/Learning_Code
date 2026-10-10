# Project: GCI World Knowledge Synthesis & Notebook-First Slide Syllabus

## Architecture
- **Educational Context**: GCI World 2026 September (Matsuo-Iwasawa Laboratory, Faculty of Engineering, The University of Tokyo).
- **Core Methodology**: DeepTutor pedagogical scaffolding (strict RFC 2119 compliance, 5-level Socratic progression, zero emojis).
- **Presentation Architecture**: Modern Reveal.js 5.1.0 loaded via pure CDN (zero local npm/build dependencies), 2D matrix navigation (horizontal Micro-Sessions, vertical topic progression), KaTeX mathematical typesetting, Atom One Dark syntax highlighting, and glassmorphic theme (#090d16 canvas).
- **3 High-Interactivity Visualizers**:
  1. NumPy Broadcasting Simulator (trailing alignment, zero-stride virtual cells, RAM conservation telemetry).
  2. ndarray Strides & Slicing Memory Visualizer (affine address mapping, live 2D grid & 1D RAM strip, view vs copy badge).
  3. Vectorization vs Python Loop Benchmark Playground (analytical SIMD model, live SVG speedup curve, race bar telemetry).
- **Notebook-First Syllabus**: Cornell 3-column note-taking system (Cues 20%, Visual Mechanism/Formulas 50%, Practical Code & Pitfalls 30%, 2-min summary box) pre-formatted for pen-and-paper writing before coding.
- **Micro-Practice Roadmap**: 15-30 minute bite-sized missions with strict Definition of Done (DoD), diagnostic self-check questions, and alignment with weekly assignments and Kaggle competition.
- **Automated Quality Suite**: 5-tier pytest suite confirming 100% pass, zero console/CDN errors, zero leftover old slides, full presence of notes and roadmaps.

## Feature Inventory
Every feature cataloged across all project phases is indexed below:

| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| F01 | 4-Step Data Science Workflow | Iterative cycle: Understanding -> Preprocessing -> Modeling -> Evaluation | M1 | prep0/1 slides, video |
| F02 | Data Classification Taxonomy | Structured vs Unstructured, Quantitative vs Qualitative types | M1 | prep1 slides, playlist |
| F03 | Missing Value Handling | Imputation (mean/mode), deletion, null audit strategies | M1 | prep1 slides, notebooks |
| F04 | Dummy Variable Encoding | One-hot encoding, dummy variable trap prevention (`drop_first=True`) | M1 | prep1 slides, notebooks |
| F05 | Feature Standardization | Z-Score transformation ($\mu=0, \sigma=1$) across heterogeneous units | M1 | prep1/3 slides, notebooks |
| F06 | Train/Test Splitting | Generalization assurance, hold-out and cross-validation | M1 | prep1/4 slides, notebooks |
| F07 | Linear Regression Modeling | Simple & multiple OLS regression, weights & bias interpretation | M1 | prep1/4 slides, notebooks |
| F08 | Decision Tree Classification | Recursive binary splitting, feature thresholds, depth control | M1 | prep4 slides, notebooks |
| F09 | K-Means Clustering | Unsupervised centroid-based clustering, Euclidean distance | M1 | prep4 slides, notes |
| F10 | Principal Component Analysis | Unsupervised dimensionality reduction, orthogonal projection | M1 | prep4 slides, notes |
| F11 | LLMs & Self-Supervised Learning | Next Token Prediction, pre-training vs fine-tuning concepts | M1 | prep4 slides, notes |
| F12 | Descriptive Statistics | Mean, Variance ($\sigma^2$), Standard Deviation ($\sigma$), dispersion | M1 | prep3 slides, notes |
| F13 | Box Plot & Quartile Analysis | Five-number summary, IQR, outlier detection ($1.5 \times \text{IQR}$) | M1 | prep3 slides, notes |
| F14 | Pearson Correlation Coefficient | Linear association $r \in [-1, 1]$, Spurious correlation warning | M1 | prep3 slides, notes |
| F15 | Regression Metric (MSE) | Mean Squared Error penalizing large residuals | M1 | prep1 slides, notebooks |
| F16 | Classification Metric (Accuracy) | Accuracy and imbalanced class pitfalls | M1 | prep1/4 slides, notebooks |
| F17 | Python OOP Foundations | Class architecture, encapsulation, `Pokemon` case study | M1 | prep2 slides, prelecture |
| F18 | Relational Table Joining | Merging tabular datasets on keys (`pd.merge(how='left')`) | M1 | classification notebooks |
| F19 | Zettabyte Data Explosion | Exponential growth (527 ZB by 2029), extraction vs storage | M2 | lec1_slides:P5, transcript |
| F20 | CRISP-DM 6-Phase Lifecycle | Business Understanding to Expansion/Deployment | M2 | lec1_slides:P7, transcript |
| F21 | Dark Data & Selection Bias | Food truck paradox, unseen data, survivor bias | M2 | lec1_slides:P7-8, transcript |
| F22 | Problem-to-Data Translation | Converting abstract business desires into KGIs/KPIs & targets | M2 | lec1_slides:P9, transcript |
| F23 | DS Competency Triad | Domain Knowledge (60-70%), Data Science, Data Engineering | M2 | lec1_slides:P10, transcript |
| F24 | Seven-Eleven Empirical Loop | Tanpin Kanri, Observe -> Hypothesize -> Experiment -> Action | M2 | lec1_slides:P12-13, transcript |
| F25 | Defensible AI Moats | Deep Workflow Integration vs vulnerable static SaaS silos | M2 | transcript [00:00:47] |
| F26 | Compound Data Flywheel | Continuous proprietary interaction data, vertical AI advantage | M2 | transcript [00:02:34] |
| F27 | 14-Week Curriculum Roadmap | 4 modular stages, timeline, milestones, capstone timing | M2 | lec1_slides:P19,25-32 |
| F28 | Ecosystem & Platform Stack | Omnicampus LMS, Google Colab, Quri AI tutor, Slack channels | M2 | lec1_slides:P20-24 |
| F29 | 3-Tier Completion Model | Completed, Honors (Top 10/20%), Outstanding (Tokyo tour) | M2 | lec1_slides:P18 |
| F30 | Course Policy & Integrity | Strict attendance survey (no late), homework penalty, GenAI policy | M2 | lec1_slides:P20-22, guides |
| F31 | ML Operational Ladder | 5-step modeling ladder and real-world evaluation | M2 | lec1_slides:P26-27 |
| F32 | Human-AI Co-Evolution | AI for parallel hypothesis falsification, human problem formulation | M2 | lec1_slides:P14,33, transcript |
| F33 | Standalone Slide Presentation Engine | Clean CSS/JS engine, Dark/Light modes, KaTeX, Mermaid, responsive | M1, M2 | survey_repo |
| F34 | Markdown Presentation Decks | Clean Marp-compatible markdown presentation source | M1, M2 | survey_repo |
| F35 | Cornell Handwritten Syllabus | 3-column note layout optimized for physical notebooks | M1, M2 | survey_repo |
| F36 | Micro-Practice Roadmap | 15-30 min Pomodoro tasks, verifiable DoD, diagnostic questions | M3 | survey_repo |
| F37 | Automated Test & Verification Suite | Pytest validation for HTML/CSS, markdown lints, formulas, DoD | M4 | survey_repo |
| F38 | ThreeUI Design System Spec | Synchronized Dark/Light palette, CSS custom properties, typography | P2-M1 | survey_threeui |
| F39 | Tri-Layer Glassmorphism & WebGL BG | WebGL shader radial vignette + CSS backdrop-filter blur(16px) | P2-M1 | survey_threeui |
| F40 | Reactive State Flow DAG Engine | Zero-dependency Signal micro-store with rAF batching (<16.6ms) | P2-M1 | survey_threeui |
| F41 | KaTeX In-Place Slot Optimization | Pre-compiled KaTeX DOM slots updating in <0.1ms with zero CLS | P2-M1 | survey_threeui |
| F42 | Dual-View Unified Controller | Single-DOM toggling between Continuous Explorable Document & Deck | P2-M1 | survey_threeui |
| F43 | Web-Native UMD/IIFE Portability | Operates under `file://` directly from USB without CORS errors | P2-M1 | survey_infra |
| F44 | Buoi 1 Food Truck Dark Data Model | Newsvendor critical fractile $F^*$, SVG Gaussian curve | P2-M2 | survey_models |
| F45 | Buoi 1 Compound Data Flywheel | 5-node interactive loop, auto-spin, Moat Depth Score | P2-M2 | survey_models |
| F46 | Buoi 1 Seven-Eleven Tanpin Kanri | 4-phase empirical restocking stepper, stance slider $\alpha$ | P2-M2 | survey_models |
| F47 | Buoi 2 NumPy Slicing & Memory Strides | C-contiguous RAM strip vs 2D grid, slice sliders, View vs Copy | P2-M3 | survey_models |
| F48 | Buoi 2 NumPy Broadcasting Visualizer | Trailing dimension alignment, zero-stride virtual expanded cells | P2-M3 | survey_models |
| F49 | Buoi 2 Vectorization Speed Simulator | N=10^2 to 10^7 slider, AVX-512 SIMD model, speedup curve | P2-M3 | survey_models |
| F50 | Cornell Notebook Blocks | 3-column note drawers for every interactive section | P2-M2, P2-M3 | survey_models |
| F51 | Extensible Boilerplates for Weeks 3+ | Boilerplate with pre-wired ThreeUIEngine for Pandas, ML loss | P2-M4 | survey_models |
| F52 | Explorable Master Hub & Navigator | `explorable/index.html` central showcase connecting all sessions | P2-M4 | survey_infra |
| F53 | Dual-Track E2E Test Suite | Tests covering Tiers 1-4 and Tier 5 adversarial tests | P2-M5 | survey_infra |
| F54 | Universal Zero-Emoji Compliance | `emoji_policy: none` enforced across all files in workspace | P2-M5 | AGENTS.md |
| F55 | Zero Regression Safety | Preservation of 100% passing status across baseline test suites | P2-M5 | survey_infra |
| F56 | Session 2 Video Knowledge Extraction | Extraction from Opening, During Lecture, and Closing videos | S3-M1 | YouTube Playlist Session 2 |
| F57 | Comprehensive Master Notes Buổi 2 | Detailed technical notes in `06_Notes_Transcripts/Lecture_02_Detailed_Notes.md` | S3-M1 | Transcripts & NumPy Docs |
| F58 | Purge Obsolete Slide Files | Remove 5 root slides in `slides/`, minimalist-deck assets, stray slides | S3-M2 | ORIGINAL_REQUEST R2 |
| F59 | Directory Restructuring & 03_Materials Population | Restructure `slides/` modularly and populate `03_Materials/` | S3-M2 | ORIGINAL_REQUEST R2 |
| F60 | Universal Link & Shortcut Re-routing | Update references in `README.md`, `INDEX.md`, `TASKS.md`, `02_Shortcuts/` | S3-M2 | ORIGINAL_REQUEST R2 |
| F61 | Micro-Learning Roadmap for Session 2 | 5-unit micro-learning roadmap (Micro-2.1 to 2.5 + Review 2.S) in `roadmap/` | S3-M3 | ORIGINAL_REQUEST R3 |
| F62 | RFC 2119 Standardized Task Management | Full task breakdown adhering to RFC 2119 and standardized schema | S3-M3 | ORIGINAL_REQUEST R3 |
| F63 | Reveal.js 5.1.0 CDN Presentation Architecture | Modern CDN-based presentation architecture with 2D navigation and HUD | S3-M4 | ORIGINAL_REQUEST R4 |
| F64 | Modern Interactive Slide Deck Buổi 0 | Modular slide deck for Buổi 0 in `slides/00_preparatory/index.html` | S3-M4 | ORIGINAL_REQUEST R4 |
| F65 | Modern Interactive Slide Deck Buổi 1 | Modular slide deck for Buổi 1 in `slides/01_orientation/index.html` | S3-M4 | ORIGINAL_REQUEST R4 |
| F66 | Modern Interactive Slide Deck Buổi 2 | Modular slide deck for Buổi 2 in `slides/02_numpy/index.html` with 3 widgets | S3-M4 | ORIGINAL_REQUEST R4 |
| F67 | Master Slide Hub Portal | Modern portal in `slides/index.html` linking all session decks | S3-M4 | ORIGINAL_REQUEST R4 |
| F68 | Interactive Widget 1: Broadcasting Simulator | Interactive shape inputs, trailing dimension alignment, zero-stride cells | S3-M4 | ORIGINAL_REQUEST R4 |
| F69 | Interactive Widget 2: ndarray Strides Visualizer | Interactive slicing, affine address formula, 2D Grid + 1D RAM, View/Copy | S3-M4 | ORIGINAL_REQUEST R4 |
| F70 | Interactive Widget 3: Vectorization Benchmark | Interactive array size slider N, live calculation comparison, curve | S3-M4 | ORIGINAL_REQUEST R4 |
| F71 | Deep Cornell Notes System Buổi 2 | 3-column Cornell format notes in `syllabus/buoi2_handwritten_notebook_syllabus.md` | S3-M5 | ORIGINAL_REQUEST R5 |
| F72 | 5-Tier Automated Quality Verification Suite | Pytest suite in `tests/test_modern_slides_and_visualizers.py` | S3-M6 | ORIGINAL_REQUEST R6 |
| F73 | Legacy Test Suite Modernization | Update `test_syllabus_and_slides.py` and `test_curriculum_matrix_and_policy.py` | S3-M6 | ORIGINAL_REQUEST R6 |
| F74 | Universal Zero-Emoji Policy Compliance | Strict verification that zero emojis exist anywhere in workspace | S3-M6 | AGENTS.md |
| F75 | 100% Automated Pytest Pass Rate | All unit and integration tests passing with 0 failures, 0 errors | S3-M6 | Acceptance Criteria |

## Milestones

| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Buổi 0 Knowledge Synthesis & Syllabus | Buổi 0 slides, handwritten syllabus, practice tasks (F01–F18, F33–F35) | Survey complete | DONE |
| M2 | Buổi 1 34-Slide Decomposition & Syllabus | Buổi 1 slides, handwritten syllabus, practice tasks (F19–F35) | Survey complete | DONE |
| M3 | Master Micro-Practice Roadmap & Cornell Guide | Integrated roadmap across Buổi 0 & 1, Cornell master guide (F36) | M1, M2 | DONE |
| M4 | E2E Review, Challenge & Forensic Integrity Audit | Multi-agent review, remediation, and Gate certification (F37) | M1, M2, M3 | DONE |
| P2-M1 | ThreeUI Design System & Core Dual-View Engine | Core reactive engine, glassmorphism styles, WebGL BG shader (F38–F43) | Survey complete | DONE |
| P2-M2 | Buổi 1 Interactive Document & Slide Deck | Food Truck (Dark Data), Data Flywheel, 7-Eleven Stepper (F44–F46, F50) | P2-M1 | DONE |
| P2-M3 | Buổi 2 Interactive Document & Slide Deck | NumPy Slicing, Strides, Broadcasting, Vectorization (F47–F50) | P2-M1 | DONE |
| P2-M4 | Cornell Boilerplates & Master Hub | Extensible templates for subsequent weeks, Master Explorable Hub (F51, F52) | P2-M2, P2-M3 | DONE |
| P2-M5 | Dual-Track E2E Test Suite & Adversarial Hardening | Comprehensive test discovery, Tiers 1-5 verification, 0 emojis (F53–F55) | P2-M1..M4 | DONE |
| P2-M6 | Final Forensic Audit & Sentinel Certification | Full forensic integrity audit, zero cheats, victory handoff | P2-M5 | DONE |
| S3-M1 | Session 2 Knowledge Extraction & Master Notes | F56, F57 (`06_Notes_Transcripts/Lecture_02_Detailed_Notes.md`) | Transcripts ready | IN_PROGRESS |
| S3-M2 | Slide Purge, Re-architecture & Link Routing | F58, F59, F60 (`slides/`, `03_Materials/`, links) | Survey complete | DONE |
| S3-M3 | Micro-Learning Roadmap & RFC 2119 Tasks | F61, F62 (`roadmap/` updates, `TASKS.md` updates) | S3-M1 | IN_PROGRESS |
| S3-M4 | Modern CDN Interactive Slide Ecosystem & 3 Visualizers | F63–F70 (Reveal.js decks Buoi 0, 1, 2 + 3 widgets) | S3-M2 | DONE |
| S3-M5 | Deep Cornell Notes System Buổi 2 | F71 (`syllabus/buoi2_handwritten_notebook_syllabus.md`) | S3-M1 | IN_PROGRESS |
| S3-M6 | Automated Quality Test Suite & Verification | F72–F75 (pytest suites, zero regression, 100% pass) | S3-M1..M5 | IN_PROGRESS |

## Interface Contracts & Layout Standards

### 1. Modern Reveal.js 5.1.0 Slide System (`slides/`)
- Pure CDN architecture: Reveal.js 5.1.0, KaTeX 0.16.9, Highlight.js 11.9.0 via jsDelivr CDN.
- 2D matrix navigation: Horizontal arrows for Micro-Sessions, Vertical arrows for deep dives and Cornell notes.
- Glassmorphic theme: `slides/css/reveal-gci-theme.css` (#090d16 canvas, Inter, JetBrains Mono).
- Visualizer widgets: `slides/css/slide-widgets.css` and `slides/js/widgets-bundle.js` / `visualizer-widgets.js`.
- Modular decks:
  * `slides/index.html` (Master Portal Hub)
  * `slides/00_preparatory/index.html` (Buoi 0 Deck)
  * `slides/01_orientation/index.html` (Buoi 1 Deck)
  * `slides/02_numpy/index.html` (Buoi 2 Deck with 3 embedded widgets)

### 2. Handwritten Cornell Notebook Syllabus (`syllabus/`)
- Header metadata: Session name, Date, Core Concept, Estimated Writing Time (15-25 min).
- 3-Column Markdown format:
  * Column 1 (20%): Keywords / Retrieval Cues / Mental Hooks.
  * Column 2 (50%): Visual Mindmaps / ASCII Schematics / Mathematical Formulas.
  * Column 3 (30%): Practical Python Actions / Code Signatures / Common Pitfalls.
- Summary Box: 2-Minute Bottom Line summarizing the core intuition.

### 3. Micro-Practice Roadmap (`roadmap/`)
- **Structure**: Every major course session (Buổi 0, Buổi 1, Buổi 2) is partitioned into 3 to 5 micro-sessions (15-30 minutes each).
- **Mandatory 2-Step Pedagogical Rhythm**:
  * Step 1 (Pen-First): Open syllabus, handwrite keywords, mindmap schematics, and formulas in notebook.
  * Step 2 (Practice & Reflection): Perform micro-practice exercises and answer diagnostic reflection questions.
- **Mandatory Review / Synthesis Session**: Each major session concludes with 1 Review & Synthesis session.

### 4. Official Materials Library (`03_Materials/`)
- `03_Materials/00_Preparatory/`: GCI Basic Learning Materials (PDF/DOCX), Pre-lecture slides & notebooks.
- `03_Materials/01_Orientation/`: `lec1_slides.pdf`.
- `03_Materials/02_NumPy/`: `lec2_slides.pdf`, `lec2_notebook.ipynb`, `HW1 for Session2.ipynb`.

### 5. ThreeUI Explorable Interactive System (`explorable/`)
- Pure web-native UMD/IIFE architecture (`window.ThreeUIEngine`). Operable via `file://` directly from USB and `http://`.
- Dual-View single-DOM toggling: `data-view="document"` (continuous scroll) vs `data-view="deck"` (16:9 presentation).
- Sub-16.6ms reactive DAG with rAF batching and KaTeX pre-compiled slots (`.dyn-slot`).

## Code Layout
```
GCI_World_2026_September/
├── 01_Recordings/               # Video bài giảng chính thức & lưu trữ
├── 02_Shortcuts/                # Lối tắt truy cập nhanh (Windows .url & macOS .webloc)
│   ├── 12_Slide_Buoi0_Preparatory (.url & .webloc)
│   ├── 13_Slide_Buoi1_Orientation (.url & .webloc)
│   ├── 14_Slide_Buoi2_NumPy_Interactive (.url & .webloc)
│   └── 18_Slides_Master_Hub (.url & .webloc)
├── 03_Materials/                # Tài liệu chính thức từ giảng viên
│   ├── 00_Preparatory/          # GCI Basic Learning Materials, Pre-lecture slides & notebooks
│   ├── 01_Orientation/          # lec1_slides.pdf
│   └── 02_NumPy/                # lec2_slides.pdf, lec2_notebook.ipynb, HW1 for Session2.ipynb
├── 04_Assignments/              # Thực hành và bài tập hàng tuần (HW1..HW8)
├── 05_Competition/              # Dự án tham gia cuộc thi Machine Learning
├── 06_Notes_Transcripts/        # Bản bóc băng YouTube Session 1 & 2 (JSON + full.md)
├── explorable/                  # Hệ thống học liệu tương tác ThreeUI Explorable
├── roadmap/                     # Lộ trình micro-learning (15-30 phút/bài) & matrix căn chỉnh
├── slides/                      # Hệ sinh thái Slide Reveal.js 5.1.0 CDN hiện đại
│   ├── index.html               # Cổng Portal điều hướng Slide Hub
│   ├── css/
│   │   ├── reveal-gci-theme.css # Theme glassmorphism và typography
│   │   └── slide-widgets.css    # Styling cho 3 widget và thẻ Cornell
│   ├── js/
│   │   ├── reveal-init.js       # Bootstrap Reveal.js 5.1.0 và keyboard HUD
│   │   ├── widgets-bundle.js    # 3 High-Interactivity Visualizer Widgets
│   │   └── visualizer-widgets.js# Alias bundle cho widget mounting
│   ├── 00_preparatory/          # Slide Buổi 0: Preparatory Foundations
│   ├── 01_orientation/          # Slide Buổi 1: Orientation & Data-Driven Mindset
│   └── 02_numpy/                # Slide Buổi 2: NumPy High Performance (tích hợp 3 widget)
├── study_notes/                 # 7 bộ ghi chú học thuật chuyên sâu
├── syllabus/                    # Sổ tay Cornell Note (3 cột: Cues, Notes, Actions + Summary)
├── tests/                       # Bộ kiểm thử tự động pytest
├── PROJECT.md                   # Đặc tả kiến trúc hệ thống và tính năng
└── README.md                    # File tổng hợp thông tin khóa học
```
