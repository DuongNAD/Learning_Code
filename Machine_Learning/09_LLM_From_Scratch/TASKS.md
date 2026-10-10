---
document_type: project_task_board
project: 09_LLM_From_Scratch
version: 1.0.0
last_updated: 2026-09-30
master_index: file:///D:/02_Learning_Knowledge/INDEX.md
focus_board: file:///D:/02_Learning_Knowledge/ACTIVE_LEARNING.md
central_tasks: file:///D:/02_Learning_Knowledge/TASKS.md
rfc2119_compliance: strict
emoji_policy: none
---

# 09_LLM_From_Scratch - Task Board

Master Knowledge Map: [INDEX.md](file:///D:/02_Learning_Knowledge/INDEX.md)
Parent Learning Hub: [Machine_Learning](file:///D:/02_Learning_Knowledge/Machine_Learning)
Learning Roadmap: [ROADMAP.md](file:///D:/02_Learning_Knowledge/Machine_Learning/09_LLM_From_Scratch/ROADMAP.md)

## Task Maintenance Rules (RFC 2119)
- Standardized Schema: All tasks MUST follow the tag format `- [ ] [Deadline: YYYY-MM-DD HH:mm] [Priority: P0/P1/P2] Description`.
- Task Preservation: AI agents MUST NEVER delete existing tasks.
- Status Transitions: Task status MUST ONLY be transitioned between `[ ]` and `[x]`, and status change to completed MUST occur ONLY IF verification criteria are met.

## 1. Environment & Baseline Setup
- [x] [Deadline: 2026-09-30 23:59] [Priority: P0] Clone repository gốc FareedKhan-dev/train-llm-from-scratch vào [00_Reference_Original](file:///D:/02_Learning_Knowledge/Machine_Learning/09_LLM_From_Scratch/00_Reference_Original).
- [x] [Deadline: 2026-09-30 23:59] [Priority: P0] Kiểm tra môi trường phần cứng NVIDIA RTX 5060 Ti (16GB VRAM) và xác thực thư viện qua [verify_environment.py](file:///D:/02_Learning_Knowledge/Machine_Learning/09_LLM_From_Scratch/03_Environment/verify_environment.py).
- [x] [Deadline: 2026-09-30 23:59] [Priority: P0] Thiết kế cấu trúc 7 chặng thực hành tự làm trong [01_Hands_On_Practice](file:///D:/02_Learning_Knowledge/Machine_Learning/09_LLM_From_Scratch/01_Hands_On_Practice).

## 2. Core Architecture Implementation (Stages 1-4)
- [x] [Deadline: 2026-10-01 23:59] [Priority: P1] Hoàn thành bài tập và kiểm thử Tokenizer & Dataloader (X, Y) trong [Stage_01_Tokenizer_Data](file:///D:/02_Learning_Knowledge/Machine_Learning/09_LLM_From_Scratch/01_Hands_On_Practice/Stage_01_Tokenizer_Data).
- [x] [Deadline: 2026-10-02 23:59] [Priority: P1] Hoàn thành bài tập và kiểm thử Causal Self-Attention & MHA trong [Stage_02_Attention](file:///D:/02_Learning_Knowledge/Machine_Learning/09_LLM_From_Scratch/01_Hands_On_Practice/Stage_02_Attention).
- [x] [Deadline: 2026-10-03 23:59] [Priority: P1] Hoàn thành bài tập và kiểm thử Transformer Block & Residual Gradient trong [Stage_03_Transformer_Block](file:///D:/02_Learning_Knowledge/Machine_Learning/09_LLM_From_Scratch/01_Hands_On_Practice/Stage_03_Transformer_Block).
- [x] [Deadline: 2026-10-04 23:59] [Priority: P1] Lắp ráp mô hình MiniGPT và thuật toán sinh Autoregressive trong [Stage_04_Full_Transformer](file:///D:/02_Learning_Knowledge/Machine_Learning/09_LLM_From_Scratch/01_Hands_On_Practice/Stage_04_Full_Transformer).

## 3. Training & Alignment Experiments (Stages 5-7)
- [x] [Deadline: 2026-10-05 23:59] [Priority: P1] Thực thi kịch bản huấn luyện MiniGPT thực chiến trong [Stage_05_Pretraining_Loop/train_mini_llm.py](file:///D:/02_Learning_Knowledge/Machine_Learning/09_LLM_From_Scratch/01_Hands_On_Practice/Stage_05_Pretraining_Loop/train_mini_llm.py).
- [x] [Deadline: 2026-10-06 23:59] [Priority: P2] Hoàn thành bài tập Chat Template & SFT Loss Masking (-100) trong [Stage_06_Supervised_FineTuning](file:///D:/02_Learning_Knowledge/Machine_Learning/09_LLM_From_Scratch/01_Hands_On_Practice/Stage_06_Supervised_FineTuning).
- [x] [Deadline: 2026-10-07 23:59] [Priority: P2] Cài đặt và kiểm thử công thức toán DPO Loss & GRPO Advantages trong [Stage_07_Alignment_RLHF](file:///D:/02_Learning_Knowledge/Machine_Learning/09_LLM_From_Scratch/01_Hands_On_Practice/Stage_07_Alignment_RLHF).

## 4. Full-Scale Exploration & Original Repository Run
- [ ] [Deadline: 2026-10-08 23:59] [Priority: P2] Chạy thử notebook tương tác [02_sft_rlhf_guide_practice.ipynb](file:///D:/02_Learning_Knowledge/Machine_Learning/09_LLM_From_Scratch/02_Interactive_Notebooks/02_sft_rlhf_guide_practice.ipynb).
- [ ] [Deadline: 2026-10-09 23:59] [Priority: P2] Chạy thử giao diện Streamlit Chat UI trong [00_Reference_Original/ui](file:///D:/02_Learning_Knowledge/Machine_Learning/09_LLM_From_Scratch/00_Reference_Original/ui).
