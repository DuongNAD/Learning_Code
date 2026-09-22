---
name: deeptutor-tutor
description: Autonomous AI Tutor and pedagogical mentor powered by DeepTutor on the portable Kingston SSD. Use when the user asks to learn a new topic, construct learning roadmaps, visualize knowledge graphs, test understanding with diagnostic quizzes, analyze learning gaps, debug coding hurdles with Socratic scaffolding, or save notes/exercises to 02_Learning_Knowledge.
metadata:
  version: v1.0.0
  publisher: Kingston-SSD-DeepTutor
---

# DeepTutor AI Tutor Skill

This skill connects Antigravity to the **DeepTutor Portable MCP Server**, running self-contained directly from the Kingston portable SSD. It equips Antigravity with research-backed pedagogical reasoning, Bloom's cognitive taxonomy, Vygotskian Socratic scaffolding, and persistent storage into your personal knowledge vault in `02_Learning_Knowledge/`.

---

## 🎯 When to Use This Skill

Trigger this skill whenever the user:
- Asks to learn, study, or understand a new programming language, framework, algorithm, or concept.
- Requests a **curriculum** or **learning roadmap** from their current level to a specific mastery goal.
- Wants a **knowledge graph** or conceptual map showing prerequisites and relationships.
- Requests **quizzes**, **practice questions**, or **flashcards** to test retention.
- Answers a question or submits code and needs **cognitive gap assessment** (diagnosing why an error occurred).
- Is stuck on a bug or coding hurdle and needs **Socratic hints** rather than immediate spoilers.
- Wants to **save learning notes, summaries, or exercise files** to `02_Learning_Knowledge/` on the portable SSD.

---

## 🛠️ DeepTutor MCP Tools (Server: `deeptutor`)

The MCP server provides the following tools:

| Tool | Purpose | Key Arguments |
|:---|:---|:---|
| `deeptutor_build_knowledge_graph` | Generate ontology, Bloom levels, prerequisites, and Mermaid diagram. | `topic` (str), `depth` (1=foundations, 2=mechanisms, 3=exhaustive) |
| `deeptutor_generate_quiz` | Create diagnostic/practice questions with distractor analysis & hints. | `topic` (str), `difficulty` ("beginner"/"intermediate"/"advanced"), `num_questions` (int), `format` ("multiple_choice"/"code_fill_or_debug"/"conceptual_short_answer"/"mixed") |
| `deeptutor_create_roadmap` | Synthesize milestone curriculum with ability contracts and exit criteria. | `topic` (str), `current_level` (str), `target_goal` (str) |
| `deeptutor_assess_gap` | Classify cognitive error type (Structural, Deviation, Application, Metacognitive). | `student_answer` (str), `expected_concept` (str) |
| `deeptutor_socratic_scaffold` | Provide 5-tier progressive hint ladder without giving away answers. | `problem_or_code` (str), `current_hurdle` (str) |
| `deeptutor_save_note` | Persist notes, flashcards, or exercises to `02_Learning_Knowledge/`. | `topic` (str), `title` (str), `content` (str), `subfolder` (str, opt) |
| `deeptutor_doctor` | Preflight diagnostic check for SSD mount point, paths, and health. | *(none)* |

---

## 🧭 Standard Pedagogical Workflows

### 1. Launching a New Learning Journey (Roadmap + Knowledge Graph)
1. **Explore the Domain**: Call `deeptutor_build_knowledge_graph` with `topic` and `depth=2`.
   - Render the `mermaid_syntax` graph in your response for visual clarity.
   - Mention any existing study materials found in `local_ssd_resources`.
2. **Synthesize the Roadmap**: Call `deeptutor_create_roadmap` with the learner's `current_level` and `target_goal`.
3. **Persist the Plan**: Call `deeptutor_save_note` with `subfolder="Roadmaps"` to save the synthesized curriculum to `02_Learning_Knowledge/<topic>/Roadmaps/`.

### 2. Active Socratic Coaching (When Learner is Stuck)
1. When a learner presents a broken snippet or is stuck on a hurdle, **DO NOT** immediately hand them the corrected code.
2. Call `deeptutor_socratic_scaffold(problem_or_code, current_hurdle)`.
3. Use the `recommended_immediate_tutor_response` (Level 1 Clarifying Observation).
4. Prompt the student to observe the state or invariant. Only advance to Level 2 (Invariant Nudge) or Level 3 (Minimal Counterexample) if they remain confused after attempting an answer.

### 3. Review & Gap Assessment (Retrieval Practice)
1. Call `deeptutor_generate_quiz` with `difficulty` and `num_questions=3`. Present questions to the learner one at a time or as a practice card.
2. When the student answers, call `deeptutor_assess_gap(student_answer, expected_concept)`.
3. Review the returned `error_type`:
   - **Structural**: Mental model is flawed. Use the returned `intuitive_analogy` to reset their baseline understanding.
   - **Deviation**: Concept is sound, but edge-case or boundary was missed. Ask the `socratic_probing_question`.
   - **Application**: Theory is right, but syntax slipped. Provide a targeted 1-line syntax refresher.
   - **Metacognitive**: Rushed assumption. Remind them of the verification step.
4. Save key takeaways or quiz reviews using `deeptutor_save_note(topic, "Quiz_Review", markdown_content, subfolder="Quizzes")`.

---

## 📁 Portable SSD Structure (`02_Learning_Knowledge`)

All notes saved via `deeptutor_save_note` dynamically resolve to the Kingston SSD mount point:
```text
<SSD_ROOT>/
├── 01_AI_Models/
├── 02_Learning_Knowledge/
│   ├── <Topic_Name>/
│   │   ├── Roadmaps/
│   │   ├── Quizzes/
│   │   └── Notes/
├── 05_Dev_Toolbox/
│   ├── DeepTutor/
│   └── Scripts/
```

Even if the SSD drive letter changes (e.g. from `D:\` to `E:\` or `/Volumes/KINGSTON`), DeepTutor's dynamic mount resolver automatically routes writes to the correct disk location.
