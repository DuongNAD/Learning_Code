import cv2
import cv2.aruco as aruco
import os

# 1. Chọn loại thư viện hỗ trợ tới 250 mã (để chứa được ID 100 và 110)
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_250)

# 2. Danh sách các ID bạn muốn tạo
target_ids = [0, 10, 100, 110]
marker_size = 400 

# Tạo thư mục để lưu ảnh cho gọn
output_folder = "aruco_markers"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

print("Đang tiến hành tạo mã...")

# 3. Vòng lặp để tạo từng mã
for m_id in target_ids:
    # Tạo ảnh marker
    marker_image = aruco.generateImageMarker(aruco_dict, m_id, marker_size)
    
    # Đặt tên file theo ID
    file_name = f"{output_folder}/marker_id_{m_id}.png"
    
    # Lưu file
    cv2.imwrite(file_name, marker_image)
    print(f" -> Đã lưu: {file_name}")

print("\nHoàn tất! Bạn hãy kiểm tra thư mục 'aruco_markers'.")