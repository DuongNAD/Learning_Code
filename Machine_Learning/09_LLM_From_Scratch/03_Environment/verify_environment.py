"""
Verification Script for LLM From Scratch Environment
Checks PyTorch, CUDA, GPU Memory, and required libraries.
"""
import sys

def check_env():
    print("=" * 60)
    print("   KIEM TRA MOI TRUONG LLM FROM SCRATCH (SSD PORTABLE)   ")
    print("=" * 60)
    print(f"Python Executable : {sys.executable}")
    print(f"Python Version    : {sys.version.split()[0]}")

    # 1. PyTorch & CUDA
    try:
        import torch
        print(f"[OK] PyTorch Version  : {torch.__version__}")
        cuda_avail = torch.cuda.is_available()
        print(f"[OK] CUDA Kha dung    : {cuda_avail}")
        if cuda_avail:
            device_name = torch.cuda.get_device_name(0)
            vram_gb = torch.cuda.get_device_properties(0).total_memory / (1024 ** 3)
            print(f"[OK] GPU Name         : {device_name}")
            print(f"[OK] VRAM Kha dung    : {vram_gb:.2f} GB")
        else:
            print("[INFO] CUDA khong kha dung, se chay che do CPU.")
    except ImportError:
        print("[FAIL] PyTorch chua duoc cai dat! Hay cai dat PyTorch truoc.")
        return False

    # 2. Cac thu vien ho tro
    libs = ["numpy", "tiktoken", "tqdm", "h5py", "datasets"]
    all_ok = True
    for lib in libs:
        try:
            __import__(lib)
            print(f"[OK] Thu vien '{lib}' da duoc cai dat.")
        except ImportError:
            print(f"[WARN] Thieu thu vien '{lib}'. Chay: pip install {lib}")
            all_ok = False

    print("=" * 60)
    if all_ok:
        print(">>> MOI TRUONG DA SAN SANG DE TU DUNG VA TRAIN LLM! <<<")
    else:
        print(">>> VUI LONG CAI DAT THEM CAC THU VIEN CAN THIEU. <<<")
    print("=" * 60)
    return all_ok

if __name__ == "__main__":
    check_env()
