import cv2
import numpy as np
import math

# =============================================================================
# 1. CẤU HÌNH THÔNG SỐ VẬT LÝ
# =============================================================================
# --- Kích thước giấy A4 (cm) ---
PAPER_W = 29.7
PAPER_H = 21.0

# --- Robot Dimensions (cm) ---
L1 = 10.5   # Bắp tay
L2 = 22.0   # Cẳng tay + Kẹp
BASE_HEIGHT = 8.5 # Chiều cao vai so với bàn

# --- Vị trí Robot (cm) ---
ROBOT_GLOBAL_X = PAPER_W / 2.0  
ROBOT_GLOBAL_Y = PAPER_H + 10.0 

# --- Cấu hình hiển thị ---
SCALE = 20  
MARGIN = 60 # Tăng lề để vẽ số
FONT = cv2.FONT_HERSHEY_PLAIN

# Màu sắc (BGR)
COLOR_BG = (30, 30, 30)
COLOR_PAPER = (255, 255, 255)
COLOR_ROBOT = (0, 165, 255)
COLOR_ARM   = (0, 255, 255)
COLOR_TARGET= (0, 0, 255)
COLOR_TEXT  = (200, 200, 200)

# =============================================================================
# 2. BỘ NÃO ROBOT (INVERSE KINEMATICS)
# =============================================================================
def solve_ik(x, y, z_table):
    z_robot = z_table - BASE_HEIGHT
    if y == 0: y = 0.001
    base_angle_rad = math.atan2(x, y)
    base_deg = 90 - math.degrees(base_angle_rad)

    r_ground = math.sqrt(x**2 + y**2) 
    D = math.sqrt(r_ground**2 + z_robot**2)

    if D > (L1 + L2):
        return None, (r_ground, z_robot)

    cos_elbow = (L1**2 + L2**2 - D**2) / (2 * L1 * L2)
    cos_elbow = max(-1.0, min(1.0, cos_elbow))
    elbow_rad = math.acos(cos_elbow)
    elbow_deg = 180 - math.degrees(elbow_rad)

    alpha = math.atan2(z_robot, r_ground)
    beta = math.acos((L1**2 + D**2 - L2**2) / (2 * L1 * D))
    shoulder_deg = math.degrees(alpha + beta)

    return (base_deg, shoulder_deg, elbow_deg), (r_ground, z_robot)

# =============================================================================
# 3. HÀM VẼ GIAO DIỆN
# =============================================================================
mouse_pos = None

def mouse_callback(event, x, y, flags, param):
    global mouse_pos
    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_pos = (x, y)

def draw_text_bg(img, text, pos, font_scale=1, color=(255,255,255), bg_color=(0,0,0)):
    """ Hàm vẽ chữ có nền đen để dễ đọc """
    x, y = pos
    (w, h), _ = cv2.getTextSize(text, FONT, font_scale, 1)
    cv2.rectangle(img, (x, y - h - 4), (x + w, y + 4), bg_color, -1)
    cv2.putText(img, text, (x, y), FONT, font_scale, color, 1)

def main():
    W_LEFT = int(PAPER_W * SCALE + MARGIN * 2)
    W_RIGHT = 500 # Mở rộng để hiển thị thông số Side View
    H_WIN = int(ROBOT_GLOBAL_Y * SCALE + MARGIN * 2)
    
    cv2.namedWindow("ROBOT SIMULATION LAB")
    cv2.setMouseCallback("ROBOT SIMULATION LAB", mouse_callback)

    while True:
        canvas = np.zeros((H_WIN, W_LEFT + W_RIGHT, 3), dtype=np.uint8)
        canvas[:] = COLOR_BG

        # ==========================
        # 1. VẼ PHẦN BÊN TRÁI (TOP-DOWN)
        # ==========================
        OX, OY = MARGIN, MARGIN
        
        # Giấy A4
        cv2.rectangle(canvas, (OX, OY), (OX + int(PAPER_W * SCALE), OY + int(PAPER_H * SCALE)), COLOR_PAPER, -1)
        
        # Thước đo trục X (Mỗi 5cm)
        for i in range(0, int(PAPER_W)+1, 5):
            px = OX + i * SCALE
            cv2.line(canvas, (px, OY), (px, OY-10), COLOR_TEXT, 1)
            cv2.putText(canvas, str(i), (px-5, OY-15), FONT, 1, COLOR_TEXT, 1)

        # Thước đo trục Y (Mỗi 5cm)
        for i in range(0, int(PAPER_H)+1, 5):
            py = OY + i * SCALE
            cv2.line(canvas, (OX, py), (OX-10, py), COLOR_TEXT, 1)
            cv2.putText(canvas, str(i), (OX-30, py+5), FONT, 1, COLOR_TEXT, 1)

        # Aruco & Robot Base
        aruco_sz = 30
        corners = [(OX, OY), (OX+int(PAPER_W*SCALE)-aruco_sz, OY),
                   (OX+int(PAPER_W*SCALE)-aruco_sz, OY+int(PAPER_H*SCALE)-aruco_sz),
                   (OX, OY+int(PAPER_H*SCALE)-aruco_sz)]
        for c in corners: cv2.rectangle(canvas, c, (c[0]+aruco_sz, c[1]+aruco_sz), (0,0,0), -1)

        RX_SCREEN = OX + int(ROBOT_GLOBAL_X * SCALE)
        RY_SCREEN = OY + int(ROBOT_GLOBAL_Y * SCALE)
        cv2.circle(canvas, (RX_SCREEN, RY_SCREEN), 15, COLOR_ROBOT, -1)
        cv2.putText(canvas, "ROBOT", (RX_SCREEN-20, RY_SCREEN+40), FONT, 1, COLOR_ROBOT, 1)

        # ==========================
        # 2. XỬ LÝ LOGIC
        # ==========================
        ik_result = None
        
        if mouse_pos:
            mx, my = mouse_pos
            if OX <= mx <= OX + int(PAPER_W*SCALE) and OY <= my <= OY + int(PAPER_H*SCALE):
                x_paper = (mx - OX) / SCALE
                y_paper = (my - OY) / SCALE
                
                # Vẽ Target & Line
                cv2.circle(canvas, (mx, my), 6, COLOR_TARGET, -1)
                cv2.line(canvas, (RX_SCREEN, RY_SCREEN), (mx, my), COLOR_ARM, 2)

                # Hiển thị tọa độ X, Y ngay tại chuột
                label = f"({x_paper:.1f}, {y_paper:.1f})"
                draw_text_bg(canvas, label, (mx + 10, my), 1.2, COLOR_TARGET, (255,255,255))
                
                # Tính toán IK
                target_x = x_paper - ROBOT_GLOBAL_X
                target_y = ROBOT_GLOBAL_Y - y_paper
                Z_PICK = 2.5
                ik_result, debug_vals = solve_ik(target_x, target_y, Z_PICK)
                
                # Info Panel
                cv2.putText(canvas, f"PAPER COORD: X={x_paper:.1f} cm, Y={y_paper:.1f} cm", (20, H_WIN - 40), FONT, 1.2, (0, 255, 0), 1)
                cv2.putText(canvas, f"ROBOT TARGET: X={target_x:.1f}, Y={target_y:.1f}, Z={Z_PICK}", (20, H_WIN - 20), FONT, 1.2, (0, 255, 255), 1)

                if ik_result:
                    b, s, e = ik_result
                    cv2.putText(canvas, f"ANGLES: Base:{b:.0f} Shldr:{s:.0f} Elbw:{e:.0f}", (20, 30), FONT, 1.5, (0, 255, 0), 2)
                else:
                    cv2.putText(canvas, "TARGET OUT OF REACH!", (20, 30), FONT, 1.5, (0, 0, 255), 2)

        # ==========================
        # 3. VẼ PHẦN BÊN PHẢI (SIDE VIEW CHI TIẾT)
        # ==========================
        SX_ORIGIN = W_LEFT + 80
        SY_ORIGIN = H_WIN - 80
        
        # Trục Z (Cao) & Y (Xa)
        cv2.arrowedLine(canvas, (SX_ORIGIN, SY_ORIGIN), (SX_ORIGIN + 350, SY_ORIGIN), (150,150,150), 2)
        cv2.arrowedLine(canvas, (SX_ORIGIN, SY_ORIGIN), (SX_ORIGIN, SY_ORIGIN - 350), (150,150,150), 2)
        cv2.putText(canvas, "Z (Height)", (SX_ORIGIN - 40, SY_ORIGIN - 340), FONT, 1, (150,150,150), 1)
        cv2.putText(canvas, "Y (Distance)", (SX_ORIGIN + 300, SY_ORIGIN + 20), FONT, 1, (150,150,150), 1)

        # Vẽ vạch thước Z (Mỗi 5cm)
        for i in range(0, 35, 5):
            py = SY_ORIGIN - int(i * SCALE)
            cv2.line(canvas, (SX_ORIGIN-5, py), (SX_ORIGIN, py), COLOR_TEXT, 1)
            cv2.putText(canvas, str(i), (SX_ORIGIN-35, py+5), FONT, 1, COLOR_TEXT, 1)

        # Vẽ Robot Base (Vai)
        BASE_H_PX = int(BASE_HEIGHT * SCALE)
        PX_VAI = (SX_ORIGIN, SY_ORIGIN - BASE_H_PX)
        
        cv2.line(canvas, (SX_ORIGIN-30, SY_ORIGIN), (SX_ORIGIN+30, SY_ORIGIN), (0,0,255), 3) # Mặt bàn
        cv2.line(canvas, (SX_ORIGIN, SY_ORIGIN), (SX_ORIGIN, SY_ORIGIN - BASE_H_PX), COLOR_ROBOT, 2) # Thân trụ
        cv2.circle(canvas, PX_VAI, 6, COLOR_ROBOT, -1)
        draw_text_bg(canvas, f"Shoulder ({BASE_HEIGHT}cm)", (PX_VAI[0]-80, PX_VAI[1]), 1, COLOR_ROBOT)

        if ik_result:
            b, s, e = ik_result
            r_ground, z_robot = debug_vals
            
            # Tính toán Forward Kinematics
            s_rad, e_rad = math.radians(s), math.radians(180 - e)
            ex = L1 * math.cos(s_rad)
            ez = L1 * math.sin(s_rad)
            
            alpha = s_rad - e_rad
            tx = ex + L2 * math.cos(alpha)
            tz = ez + L2 * math.sin(alpha)
            
            # Tọa độ màn hình
            PX_KHUYU = (SX_ORIGIN + int(ex*SCALE), SY_ORIGIN - BASE_H_PX - int(ez*SCALE))
            PX_TIP   = (SX_ORIGIN + int(tx*SCALE), SY_ORIGIN - BASE_H_PX - int(tz*SCALE))
            
            # Vẽ cánh tay
            cv2.line(canvas, PX_VAI, PX_KHUYU, COLOR_ARM, 4)
            cv2.line(canvas, PX_KHUYU, PX_TIP, COLOR_ARM, 4)
            
            # HIỂN THỊ GIÁ TRỊ TẠI CÁC KHỚP (FEATURE MỚI)
            # 1. Tại Khuỷu
            elbow_z_real = BASE_HEIGHT + ez
            draw_text_bg(canvas, f"Elbow H:{elbow_z_real:.1f}", (PX_KHUYU[0]+10, PX_KHUYU[1]), 1, COLOR_ARM)
            cv2.circle(canvas, PX_KHUYU, 5, (0,0,255), -1)

            # 2. Tại Đầu kẹp (Tip)
            tip_z_real = BASE_HEIGHT + tz
            tip_y_real = tx # Khoảng cách vươn xa tính từ trục vai
            draw_text_bg(canvas, f"Tip Z:{tip_z_real:.1f}", (PX_TIP[0]+10, PX_TIP[1]), 1, (0,255,0))
            draw_text_bg(canvas, f"Reach:{tip_y_real:.1f}", (PX_TIP[0]+10, PX_TIP[1]+20), 1, (0,255,0))
            cv2.circle(canvas, PX_TIP, 5, (0,255,0), -1)

            # Vẽ đường gióng xuống đất để xem tầm vươn xa
            cv2.line(canvas, PX_TIP, (PX_TIP[0], SY_ORIGIN), (50,50,50), 1, cv2.LINE_AA)
            cv2.putText(canvas, f"{r_ground:.1f}cm", (PX_TIP[0]-20, SY_ORIGIN+20), FONT, 1, COLOR_TARGET, 1)

        cv2.imshow("ROBOT SIMULATION LAB", canvas)
        if cv2.waitKey(1) == ord('q'): break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()