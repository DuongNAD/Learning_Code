# 🚀 09_LLM_From_Scratch: Xây Dựng & Huấn Luyện Mô Hình Ngôn Ngữ Lớn Từ Đầu

[![PyTorch](https://img.shields.io/badge/PyTorch-2.8%2B-EE4C2C.svg?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![CUDA](https://img.shields.io/badge/CUDA-Enabled-76B900.svg?logo=nvidia&logoColor=white)](https://developer.nvidia.com/cuda-toolkit)
[![Hardware](https://img.shields.io/badge/GPU-RTX%205060%20Ti%20(16GB)-green.svg)](file:///D:/02_Learning_Knowledge/Machine_Learning/09_LLM_From_Scratch/03_Environment/verify_environment.py)
[![Origin](https://img.shields.io/badge/Upstream-FareedKhan--dev-blue.svg)](https://github.com/FareedKhan-dev/train-llm-from-scratch)

Không gian học tập và thực hành toàn diện về **Large Language Models (LLMs) từ con số 0 (From Scratch)** hoàn toàn bằng thuần **PyTorch** (không dùng HuggingFace Transformers, không dùng TRL, không dùng PEFT).

Dự án đưa bạn đi trọn vẹn hành trình từ **Văn bản thô (Raw text)** đến **Mô hình lập luận căn chỉnh hoàn chỉnh (Aligned Reasoning LLM)**:
$$\text{Raw Text} \rightarrow \text{Tokens} \rightarrow \text{Transformer} \rightarrow \text{Base Model} \rightarrow \text{SFT} \rightarrow \text{Reward Model} \rightarrow \text{DPO / PPO} \rightarrow \text{GRPO (DeepSeek-R1)} \rightarrow \text{Chat UI}$$

---

## 🗂️ Cấu trúc Không gian Học tập & Tự làm (Directory Architecture)

```text
09_LLM_From_Scratch/
├── README.md                          # Tài liệu tổng quan & hướng dẫn nhập môn
├── ROADMAP.md                         # Lộ trình 7 giai đoạn học và tự code từ A-Z
├── TASKS.md                           # Bảng theo dõi tiến độ thực hành chuẩn [ ] / [x]
├── GEMINI.md / AGENTS.md              # Chỉ thị DeepTutor AI Mentor (hỗ trợ giải thích, không spoil code)
│
├── 📂 00_Reference_Original/          # CODE GỐC CHUẨN CỦA TÁC GIẢ (Fareed Khan)
│   ├── .git/                          # Giữ nguyên Git repository để `git pull` update mới nhất
│   ├── src/models/                    # Attention, MLP, TransformerBlock, Transformer
│   ├── src/post_training/             # SFT, Reward Model, DPO, PPO, GRPO, Evaluation
│   ├── scripts/                       # Scripts tiền xử lý, huấn luyện, sinh text, chat CLI
│   ├── configs/                       # Cấu hình YAML cho pretrain, sft, dpo, ppo, grpo
│   ├── tests/                         # Bộ unit test của tác giả
│   ├── ui/                            # Giao diện Chat Web với Streamlit
│   └── sft_rlhf_guide.ipynb           # Notebook gốc hướng dẫn SFT & RLHF
│
├── 🛠️ 01_Hands_On_Practice/          # KHÔNG GIAN DÀNH CHO BẠN "TỰ LÀM" (DIY Code-Along)
│   ├── Stage_01_Tokenizer_Data/       # Giai đoạn 1: BPE / Tokenizer & Dataloader (X, Y)
│   ├── Stage_02_Attention/            # Giai đoạn 2: Scaled Dot-Product, Causal Mask & MHA
│   ├── Stage_03_Transformer_Block/    # Giai đoạn 3: Pre-LayerNorm, GELU/MLP & Residual Highway
│   ├── Stage_04_Full_Transformer/     # Giai đoạn 4: MiniGPT hoàn chỉnh & Thuật toán sinh Autoregressive
│   ├── Stage_05_Pretraining_Loop/     # Giai đoạn 5: Vòng lặp Pretraining, Loss Cross-Entropy, Optimizer
│   ├── Stage_06_Supervised_FineTuning/# Giai đoạn 6: Chat Template & SFT Loss Masking (-100)
│   └── Stage_07_Alignment_RLHF/       # Giai đoạn 7: Căn chỉnh nâng cao (DPO Loss & GRPO Advantages)
│
├── 📓 02_Interactive_Notebooks/       # Jupyter Notebooks tương tác & Trực quan hóa
│   ├── visualize_attention_matrix.py  # Script in biểu đồ nhiệt ma trận chú ý (Causal Mask)
│   └── 02_sft_rlhf_guide_practice.ipynb # Notebook thực hành chi tiết
│
└── ⚙️ 03_Environment/                 # Môi trường thực thi & Kiểm tra phần cứng
    ├── requirements.txt               # Danh sách thư viện cần thiết
    └── verify_environment.py          # Script kiểm tra GPU NVIDIA RTX 5060 Ti & PyTorch
```

---

## ⚡ Bắt Đầu Nhanh (Quickstart)

### 1. Kiểm tra môi trường & GPU
Chạy script kiểm tra trong `03_Environment`:
```powershell
python 03_Environment/verify_environment.py
```
*(Hệ thống đã xác nhận GPU **NVIDIA GeForce RTX 5060 Ti** với 16GB VRAM và CUDA 12.8 sẵn sàng!)*

### 2. Thực hành từng giai đoạn trong `01_Hands_On_Practice/`
Mỗi giai đoạn được thiết kế độc lập gồm:
1. `notes.md`: Tóm tắt toán học và trực giác bản chất.
2. `exercise_*.py`: Khung code để bạn tự điền logic (chứa `# TODO:` hướng dẫn).
3. `test_*.py`: Bộ unit test tự động chấm điểm code bạn viết.

Ví dụ: Bắt đầu ngay với Giai đoạn 1:
```powershell
cd 01_Hands_On_Practice/Stage_01_Tokenizer_Data
python test_data.py
```

### 3. Huấn luyện thử mô hình MiniGPT trong 5 giây!
Để thấy mô hình tự học ngôn ngữ ngay trên GPU của bạn:
```powershell
cd 01_Hands_On_Practice/Stage_05_Pretraining_Loop
python train_mini_llm.py
```

---

## 🔄 Cập nhật mã nguồn gốc từ Github
Khi tác giả Fareed Khan có cập nhật mới trên kho mã nguồn gốc:
```powershell
cd 00_Reference_Original
git pull origin main
```
Toàn bộ code tự làm và bài tập của bạn trong `01_Hands_On_Practice` hoàn toàn tách biệt nên không bao giờ lo bị xung đột hay mất mát dữ liệu!
