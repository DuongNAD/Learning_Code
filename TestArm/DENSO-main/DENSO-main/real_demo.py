import cv2
import numpy as np
import time
import cv2.aruco as aruco
from ultralytics import YOLO
from robot_new_2 import RobotArm 

# =============================================================================
# 1. CẤU HÌNH HỆ THỐNG (GIẤY NGANG - LANDSCAPE)
# =============================================================================
PAPER_WIDTH_CM  = 29.7
PAPER_HEIGHT_CM = 21.0

# Vị trí Robot (Theo sơ đồ anh vẽ: Giữa chiều ngang, cách đáy 10cm)
ROBOT_GLOBAL_X = PAPER_WIDTH_CM / 2.0   # 14.85 cm
ROBOT_DIST_FROM_PAPER = 10.0

# [ĐÃ SỬA TÊN BIẾN]: ROBOT_GLOBAL_Z (Thay cho Y cũ) - Khoảng cách theo trục sâu
ROBOT_GLOBAL_Z = PAPER_HEIGHT_CM + ROBOT_DIST_FROM_PAPER # 31.0 cm

# ID Aruco 4 góc (Trên-Trái, Trên-Phải, Dưới-Phải, Dưới-Trái)
ID_TL, ID_TR, ID_BR, ID_BL = 0, 10, 100, 110 

Y_PICK = 2.5       # Độ cao gắp (cm) - Trục Y hướng lên trời
Y_SAFE = 10.0      # Độ cao an toàn di chuyển
GRIP_OPEN  = 30
GRIP_CLOSE = 68

# =============================================================================
# 2. KHỞI TẠO
# =============================================================================
print("[INIT] Đang khởi tạo hệ thống...")

# Robot
try:
    robot = RobotArm(port="COM9", baudrate=9600) 
except:
    robot = None

# Model YOLO
try:
    model = YOLO("best_1.pt")
except:
    print("[ERROR] Thiếu file 'best_1.pt'")
    exit()

# Camera
cap = cv2.VideoCapture(0) # Đổi thành 1 nếu dùng Cam rời
cap.set(3, 640)
cap.set(4, 480)

# Aruco (Hỗ trợ mọi phiên bản OpenCV)
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_250)
try:
    aruco_params = aruco.DetectorParameters()
except AttributeError:
    aruco_params = aruco.DetectorParameters_create()

last_action_time = 0
COOLDOWN_TIME = 5.0 

# =============================================================================
# 3. HÀM XỬ LÝ
# =============================================================================
def get_perspective_transform(frame, corners, ids):
    if ids is None: return None, None
    centers = {}
    for i, m_id in enumerate(ids):
        c = corners[i][0]
        cx = int((c[0][0] + c[2][0]) / 2)
        cy = int((c[0][1] + c[2][1]) / 2)
        centers[m_id[0]] = (cx, cy)

    if all(k in centers for k in [ID_TL, ID_TR, ID_BR, ID_BL]):
        src = np.array([centers[ID_TL], centers[ID_TR], centers[ID_BR], centers[ID_BL]], dtype="float32")
        SCALE = 20 # 1cm = 20px
        w_px = int(PAPER_WIDTH_CM * SCALE)
        h_px = int(PAPER_HEIGHT_CM * SCALE)
        dst = np.array([[0,0], [w_px,0], [w_px,h_px], [0,h_px]], dtype="float32")
        M = cv2.getPerspectiveTransform(src, dst)
        return M, SCALE
    return None, None

# =============================================================================
# 4. VÒNG LẶP CHÍNH
# =============================================================================
print("[READY] Đưa giấy A4 vào camera...")

while True:
    ret, frame = cap.read()
    if not ret: break

    # 1. Tìm Aruco
    corners, ids, _ = aruco.detectMarkers(frame, aruco_dict, parameters=aruco_params)
    M, px_per_cm = get_perspective_transform(frame, corners, ids)
    
    if M is not None:
        cv2.putText(frame, "A4 LOCKED", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # 2. Tìm vật (YOLO)
        results = model(frame, verbose=False, stream=True)
        for result in results:
            boxes = result.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                conf = box.conf[0]
                
                if conf > 0.6:
                    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 255), 2)
                    
                    # 3. Tính tọa độ CM trên giấy
                    cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
                    pt = cv2.perspectiveTransform(np.array([[[cx, cy]]], dtype="float32"), M)

                    obj_x_paper = pt[0][0][0] / px_per_cm
                    obj_z_paper = pt[0][0][1] / px_per_cm # Trục dọc trên giấy là Z (Sâu)
                    
                    # 4. Tính tọa độ Robot
                    # Robot nằm giữa chiều ngang -> X = 0
                    target_x = obj_x_paper - ROBOT_GLOBAL_X
                    
                    # Công thức: Tổng khoảng cách từ Robot đến đỉnh giấy - Vị trí Z trên giấy
                    target_z = ROBOT_GLOBAL_Z - obj_z_paper
                    
                    # Hiển thị đúng hệ trục anh muốn: X (Ngang), Z (Sâu)
                    info = f"X:{target_x:.1f} Z:{target_z:.1f}"
                    cv2.putText(frame, info, (int(x1), int(y1)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

                    # 5. Gửi lệnh Robot (Mapping sang Driver)
                    if (time.time() - last_action_time > COOLDOWN_TIME):
                        # Log ra màn hình đúng hệ tọa độ anh muốn (Y là chiều cao)
                        print(f"\n[ACTION] Gắp tại: X={target_x:.1f}, Z={target_z:.1f}, Y_Height={Y_PICK}")
                        
                        if robot:
                            # --- MAPPING QUAN TRỌNG ---
                            # Hàm move_to trong driver nhận (x, reach, height)
                            # Chúng ta truyền: (target_x, target_z, Y_SAFE)
                            
                            # B1: Đến vị trí chờ (steps=20: Tốc độ vừa)
                            robot.move_to(target_x, target_z, Y_SAFE, GRIP_OPEN, steps=20)
                            time.sleep(1.0)
                            
                            # B2: Hạ trục Y xuống (steps=50: Rất chậm & chuẩn)
                            print("... Ha truc Y xuong ...")
                            robot.move_to(target_x, target_z, Y_PICK, GRIP_OPEN, steps=50)
                            time.sleep(1.0)
                            
                            # B3: Đóng kẹp (steps=10: Nhanh)
                            robot.move_to(target_x, target_z, Y_PICK, GRIP_CLOSE, steps=10)
                            time.sleep(0.5)
                            
                            # B4: Nhấc trục Y lên (steps=40: Chậm để không rơi)
                            print("... Nhac truc Y len ...")
                            robot.move_to(target_x, target_z, Y_SAFE, GRIP_CLOSE, steps=40)
                            time.sleep(1.0)
                            
                            # B5: Về nhà (Về vị trí chờ an toàn)
                            print("... Ve nha ...")
                            robot.send_cmd(90, 90, 45, GRIP_CLOSE)
                        
                        last_action_time = time.time()
    else:
        cv2.putText(frame, "Tim 4 ma Aruco...", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Robot Vision", frame)
    if cv2.waitKey(1) == ord('q'): break

cap.release()
cv2.destroyAllWindows()
if robot: robot.close()