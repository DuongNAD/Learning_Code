import cv2
import numpy as np
import math
from ultralytics import YOLO

# =================================================================================
# 1. CẤU HÌNH HỆ THỐNG (ANH SỬA THÔNG SỐ Ở ĐÂY CHO KHỚP THỰC TẾ)
# =================================================================================

# --- Kích thước cửa sổ giả lập ---
IMG_W, IMG_H = 1280, 720 

# --- Thông số Robot thực tế (Đo bằng thước) ---
LINK_1 = 14.0       # cm (Độ dài bắp tay - từ vai đến khuỷu)
LINK_2 = 14.0       # cm (Độ dài cẳng tay - từ khuỷu đến cổ tay)
ROBOT_BASE_X = 15.0 # cm (Robot đặt ở giữa chiều ngang bàn)
ROBOT_BASE_Z = -5.0 # cm (Robot đặt lùi về sau mép giấy 5cm)

# --- Thông số bàn làm việc (Tờ giấy A4 in ArUco) ---
PAPER_W = 27.7      # cm (Chiều ngang vùng làm việc)
PAPER_H = 19.0      # cm (Chiều dọc vùng làm việc)

# --- Vị trí 4 góc bàn trên màn hình (Giả lập góc nhìn Camera) ---
# Anh có thể chỉnh các số này để làm méo hình, test độ xịn của thuật toán
TL_PX = (250, 150)  # Top-Left
TR_PX = (1030, 150) # Top-Right
BR_PX = (1150, 600) # Bottom-Right
BL_PX = (130, 600)  # Bottom-Left

# =================================================================================
# 2. CLASS ROBOT ẢO (TÍNH TOÁN & VẼ)
# =================================================================================
class VirtualRobot:
    def __init__(self):
        # Tọa độ các khớp (cm)
        self.base_x, self.base_z = ROBOT_BASE_X, ROBOT_BASE_Z
        self.elbow_x, self.elbow_z = 0, 0
        self.end_x, self.end_z = 0, 0
        self.reachable = False

    def solve_ik_2d(self, target_x, target_z):
        """
        Giải thuật Inverse Kinematics 2D (Planar) dùng định lý hàm Cos
        Mục đích: Tính góc vai và khuỷu để đầu kẹp chạm target_x, target_z
        """
        # Dời gốc tọa độ về vai robot
        dx = target_x - self.base_x
        dz = target_z - self.base_z
        dist = math.sqrt(dx**2 + dz**2)

        # Kiểm tra tầm vươn (Reach)
        max_reach = LINK_1 + LINK_2
        
        if dist > max_reach:
            self.reachable = False
            # Nếu không với tới, vươn thẳng tay về hướng đó
            ratio = max_reach / dist
            self.end_x = self.base_x + dx * ratio
            self.end_z = self.base_z + dz * ratio
            # Khuỷu tay nằm giữa
            self.elbow_x = self.base_x + dx * 0.5 * ratio
            self.elbow_z = self.base_z + dz * 0.5 * ratio
        else:
            self.reachable = True
            # Áp dụng định lý hàm số Cos
            # alpha: Góc phụ tại vai
            # theta: Góc nâng vai
            c = dist
            a = LINK_1
            b = LINK_2
            
            try:
                cos_alpha = (a**2 + c**2 - b**2) / (2 * a * c)
                alpha = math.acos(max(-1.0, min(1.0, cos_alpha))) # Kẹp giá trị an toàn
                
                base_angle = math.atan2(dz, dx) # Góc hướng tới mục tiêu
                theta1 = base_angle - alpha     # Góc vai thực tế
                
                # Tính tọa độ khuỷu tay
                self.elbow_x = self.base_x + a * math.cos(theta1)
                self.elbow_z = self.base_z + a * math.sin(theta1)
                
                # Đầu kẹp trùng mục tiêu
                self.end_x = target_x
                self.end_z = target_z
            except:
                self.reachable = False

    def draw(self, img, H_world_to_pixel):
        """Vẽ cánh tay lên màn hình giả lập"""
        def to_px(x, z):
            pt = np.array([[[x, z]]], dtype=np.float32)
            px = cv2.perspectiveTransform(pt, H_world_to_pixel)[0][0]
            return (int(px[0]), int(px[1]))

        # Chuyển đổi tọa độ cm -> pixel
        p_base = to_px(self.base_x, self.base_z)
        p_elbow = to_px(self.elbow_x, self.elbow_z)
        p_end = to_px(self.end_x, self.end_z)

        # Màu sắc: Xanh lá nếu với tới, Đỏ nếu không
        color = (0, 255, 0) if self.reachable else (0, 0, 255)
        thick = 6

        # Vẽ Link 1 (Vai -> Khuỷu)
        cv2.line(img, p_base, p_elbow, (255, 255, 0), thick) 
        # Vẽ Link 2 (Khuỷu -> Tay)
        cv2.line(img, p_elbow, p_end, color, thick)
        
        # Vẽ khớp
        cv2.circle(img, p_base, 12, (50, 50, 50), -1)  # Đế
        cv2.circle(img, p_elbow, 10, (0, 0, 255), -1)  # Khuỷu
        cv2.circle(img, p_end, 15, color, -1)          # Kẹp
        cv2.circle(img, p_end, 5, (0,0,0), -1)         # Tâm kẹp

# =================================================================================
# 3. CÁC HÀM HỖ TRỢ ĐỒ HỌA
# =================================================================================
def create_aruco_marker(id, size=100):
    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_1000)
    img = cv2.aruco.generateImageMarker(dictionary, id, size)
    return cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

def overlay_image(bg, fg, x, y):
    h, w = fg.shape[:2]
    if y+h > bg.shape[0] or x+w > bg.shape[1]: return
    bg[y:y+h, x:x+w] = fg

# =================================================================================
# 4. CHƯƠNG TRÌNH CHÍNH (MAIN LOOP)
# =================================================================================
def main():
    print("--- KHỞI TẠO SIMULATION ---")
    
    # 1. Load Model (Giả lập)
    try:
        model = YOLO("best_1.pt")
        print("✅ Đã load model 'best_1.pt'")
    except:
        print("⚠️ Không thấy 'best_1.pt'. Chạy chế độ Mock Model.")
        model = None

    robot = VirtualRobot()

    # 2. Tạo Marker ArUco
    m0   = create_aruco_marker(0, 80)
    m100 = create_aruco_marker(100, 80)
    m110 = create_aruco_marker(110, 80)
    m10  = create_aruco_marker(10, 80)

    # 3. Tính toán Ma trận Homography
    # Điểm nguồn (Thực tế - cm)
    src_pts = np.array([
        [1.0, 1.0],           # Top-Left
        [PAPER_W-1.0, 1.0],   # Top-Right
        [PAPER_W-1.0, PAPER_H-1.0], # Bottom-Right
        [1.0, PAPER_H-1.0]    # Bottom-Left
    ], dtype=np.float32)

    # Điểm đích (Màn hình - pixel)
    dst_pts = np.array([TL_PX, TR_PX, BR_PX, BL_PX], dtype=np.float32)

    # Ma trận chuyển đổi
    H_pixel_to_world = cv2.findHomography(dst_pts, src_pts)[0] # Vision dùng cái này
    H_world_to_pixel = cv2.findHomography(src_pts, dst_pts)[0] # Giả lập dùng cái này để vẽ

    # 4. Biến trạng thái
    sim_box_x = 15.0 # Vị trí hộp ban đầu (cm)
    sim_box_z = 10.0
    step = 0.5 # Bước di chuyển

    print("\n🎮 HƯỚNG DẪN:")
    print("   👉 W / S : Di chuyển hộp Xa / Gần")
    print("   👉 A / D : Di chuyển hộp Trái / Phải")
    print("   👉 Q     : Thoát")

    while True:
        # --- A. RENDER MÔI TRƯỜNG ---
        frame = np.ones((IMG_H, IMG_W, 3), dtype=np.uint8) * 40 # Nền xám tối

        # Vẽ khung bàn làm việc
        cv2.polylines(frame, [dst_pts.astype(np.int32)], True, (0, 255, 0), 2)
        
        # Dán 4 ArUco vào 4 góc
        overlay_image(frame, m0,   TL_PX[0]-40, TL_PX[1]-40)
        overlay_image(frame, m100, TR_PX[0]-40, TR_PX[1]-40)
        overlay_image(frame, m110, BR_PX[0]-40, BR_PX[1]-40)
        overlay_image(frame, m10,  BL_PX[0]-40, BL_PX[1]-40)

        # --- B. GIẢ LẬP HỘP & VISION ---
        # 1. Tính vị trí pixel của hộp từ tọa độ thật (Simulation Logic)
        box_world_pt = np.array([[[sim_box_x, sim_box_z]]], dtype=np.float32)
        box_px_pt = cv2.perspectiveTransform(box_world_pt, H_world_to_pixel)[0][0]
        bx, by = int(box_px_pt[0]), int(box_px_pt[1])

        # 2. Vẽ cái hộp lên màn hình (Màu đỏ)
        cv2.rectangle(frame, (bx-30, by-30), (bx+30, by+30), (0, 0, 255), -1)
        cv2.putText(frame, "TARGET", (bx-25, by-40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200,200,255), 2)

        # 3. "Vision Pipeline" (Thực hiện tính toán ngược lại để kiểm chứng)
        # Giả sử Camera nhìn thấy hộp ở (bx, by), giờ tính ra tọa độ cm
        vision_pt = cv2.perspectiveTransform(np.array([[[bx, by]]], dtype=np.float32), H_pixel_to_world)[0][0]
        calc_x, calc_z = vision_pt[0], vision_pt[1]

        # --- C. ROBOT LOGIC (INVERSE KINEMATICS) ---
        # Ra lệnh cho robot vươn tới tọa độ vừa tính được
        robot.solve_ik_2d(calc_x, calc_z)
        robot.draw(frame, H_world_to_pixel)

        # --- D. HIỂN THỊ THÔNG TIN ---
        # Thông tin Tọa độ
        cv2.putText(frame, f"TRUE POS (Sim):  X={sim_box_x:.1f}  Z={sim_box_z:.1f}", (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        cv2.putText(frame, f"VISION CALC:     X={calc_x:.1f}  Z={calc_z:.1f}", (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # Thông tin Trạng thái Robot
        if robot.reachable:
            status = "STATUS: REACHABLE (OK)"
            color = (0, 255, 0)
        else:
            status = "STATUS: OUT OF RANGE (XA QUA!)"
            color = (0, 0, 255)
        
        cv2.putText(frame, status, (30, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        # --- E. XỬ LÝ PHÍM BẤM ---
        cv2.imshow("ROBOT ARM SIMULATION TESTBENCH", frame)
        key = cv2.waitKey(20) & 0xFF

        if key == ord('q'): break
        
        # Điều khiển hộp
        if key == ord('w'): sim_box_z -= step # Đi xa (theo trục Z của giấy)
        if key == ord('s'): sim_box_z += step # Đi gần
        if key == ord('a'): sim_box_x -= step # Sang trái
        if key == ord('d'): sim_box_x += step # Sang phải

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()