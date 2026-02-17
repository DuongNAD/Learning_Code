import soundfile as sf
import noisereduce as nr
import librosa
import numpy as np
import scipy.signal

# Tên file
input_file = "Recording (2).mp3"
output_file = "Recording_V2_Natural.wav"

print(f"🔄 Đang xử lý file: {input_file}...")

# 1. Load file
data, rate = librosa.load(input_file, sr=None)

# 2. Khử ồn (ĐÃ ĐIỀU CHỈNH)
# - prop_decrease=0.60: Chỉ giảm 60% tiếng ồn (thay vì 95%).
#   Mục đích: Giữ lại một xíu nền để giọng nói nghe thật hơn, không bị méo.
# - n_fft=2048: Tăng độ phân giải tần số để tách giọng trầm tốt hơn.
clean_data = nr.reduce_noise(
    y=data,
    sr=rate,
    stationary=True,
    prop_decrease=0.60,  # GIẢM TỪ 0.95 XUỐNG 0.60
    n_fft=2048,
    n_std_thresh_stationary=1.5 # Tăng ngưỡng an toàn để không cắt nhầm giọng
)

# 3. Lọc tần số thấp (High-Pass Filter)
# Giữ nguyên bước này vì nó rất tốt để loại bỏ tiếng ầm ầm
sos = scipy.signal.butter(4, 80, 'hp', fs=rate, output='sos')
filtered_data = scipy.signal.sosfilt(sos, clean_data)

# 4. Chuẩn hóa âm lượng (Normalization)
max_val = np.max(np.abs(filtered_data))
target_level = 0.95
normalized_data = filtered_data / max_val * target_level

# 5. Xuất file
sf.write(output_file, normalized_data, rate)

print(f"✅ Xong! Hãy nghe thử file: {output_file}")