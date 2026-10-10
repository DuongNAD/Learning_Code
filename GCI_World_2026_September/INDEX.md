# GCI World 2026 September · Master Knowledge Map & Index

Course: GCI World (Global Consumer Intelligence / Data Science & AI)
Institution: Matsuo-Iwasawa Laboratory, Graduate School of Engineering, The University of Tokyo
Compliance: emoji_policy: none (Zero Unicode Emojis), strict RFC 2119

---

## 1. Quick Navigation Hub

| Section | Directory / Link | Description |
| :--- | :--- | :--- |
| **Master Slide Hub** | [slides/index.html](slides/index.html) | Modern Reveal.js 5.1.0 CDN slide portal |
| **Slide Buoi 0** | [slides/00_preparatory/index.html](slides/00_preparatory/index.html) | Preparatory Foundations (DS cycle, stats, OOP) |
| **Slide Buoi 1** | [slides/01_orientation/index.html](slides/01_orientation/index.html) | Orientation, CRISP-DM, Dark Data, AI Moats |
| **Slide Buoi 2** | [slides/02_numpy/index.html](slides/02_numpy/index.html) | NumPy High Performance + 3 Interactive Widgets |
| **Explorable Document** | [explorable/index.html](explorable/index.html) | ThreeUI reactive explorable document system |
| **Official Materials** | [03_Materials/](03_Materials/) | Session PDFs and Jupyter Notebooks (00, 01, 02) |
| **Assignments & Code** | [04_Assignments/](04_Assignments/) | Practical benchmarks, HW1..HW8 exercises |
| **Transcripts & Notes** | [06_Notes_Transcripts/](06_Notes_Transcripts/) | Full YouTube transcripts & lecture synthesis |
| **Roadmap v2 (start here)** | [roadmap/ROADMAP.md](roadmap/ROADMAP.md) | 14-session plan: verified schedule and completion rules, modules with self-tests, spaced review, competition and final assignment |
| **Micro-Roadmap (old)** | [roadmap/micro_practice_roadmap.md](roadmap/micro_practice_roadmap.md) | Superseded by ROADMAP.md; sessions 0-2 micro-missions only |
| **Cornell Syllabi** | [syllabus/](syllabus/) | Handwritten notebook 3-column Cornell syllabi |
| **Desktop Shortcuts** | [02_Shortcuts/](02_Shortcuts/) | 1-click access shortcuts (.url and .webloc) |

---

## 2. Interactive Visualizer Widgets Index

1. **Widget 1: NumPy Broadcasting Rules Simulator**
   - Location: Embedded in `slides/02_numpy/index.html` (Micro-Session 3)
   - Capabilities: Trailing dimension alignment, zero-stride memory detection (`stride=0`), RAM conservation metrics, incompatible error simulation.
2. **Widget 2: ndarray Memory Strides & Slicing Visualizer**
   - Location: Embedded in `slides/02_numpy/index.html` (Micro-Session 1)
   - Capabilities: Interactive row/col sliders, affine address formula, synchronized 2D logical grid and 1D physical RAM strip, View (0 Bytes) vs Copy badge.
3. **Widget 3: SIMD Vectorization vs Python Loop Benchmark**
   - Location: Embedded in `slides/02_numpy/index.html` (Micro-Session 4)
   - Capabilities: Slider $N \in [10^2, 10^7]$, analytical model ($T_{\text{py}}$ vs $T_{\text{np}}$), live SVG performance curve, AVX-512 asymptote ceiling (~297.6x), animated race track.

---

## 3. Session Topology & Materials Breakdown

### Session 0: Preparatory Foundations
- Slides: `slides/00_preparatory/index.html`
- Materials: `03_Materials/00_Preparatory/GCI Basic Learning Materials.pdf`, `prelecture_slides.pdf`, `prelecture_notebook.ipynb`
- Syllabus: `syllabus/buoi0_handwritten_notebook_syllabus.md`

### Session 1: Orientation & Data-Driven Mindset
- Slides: `slides/01_orientation/index.html`
- Materials: `03_Materials/01_Orientation/lec1_slides.pdf`
- Transcripts: `06_Notes_Transcripts/Session_01_Official_YouTube_transcript_full.md`
- Syllabus: `syllabus/buoi1_handwritten_notebook_syllabus.md`

### Session 2: NumPy & Multi-Dimensional Computing
- Slides: `slides/02_numpy/index.html`
- Materials: `03_Materials/02_NumPy/lec2_slides.pdf`, `lec2_notebook.ipynb`, `HW1 for Session2.ipynb`
- Transcripts: `06_Notes_Transcripts/GCI_World_Session_02_Opening_transcript_full.md`, `During_Lecture`, `Closing`
- Syllabus: `syllabus/buoi2_handwritten_notebook_syllabus.md`
