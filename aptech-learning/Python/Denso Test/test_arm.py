import math
import time
import serial

# =================================================================================
# 1. CẤU HÌNH KÍCH THƯỚC & PHẦN CỨNG
# =================================================================================

# --- A. Kích thước 3 đoạn (Đo lại từ thực tế) ---
L1 = 10.5  # Bắp tay (Vai -> Khuỷu)
L2 = 9.0  # Cẳng tay (Khuỷu -> Cổ tay)
L3 = 6.5  # Bàn tay (Cổ tay -> Đầu kẹp)

# --- B. Cân chỉnh Servo (Offset) ---
# Anh chỉnh số ở đây để robot thẳng hàng
BASE_OFFSET = 0
SHOULDER_OFFSET = 15  # Nâng vai
ELBOW_OFFSET = -10  # Chỉnh khuỷu
WRIST_OFFSET = 0  # <--- MỚI: Chỉnh cổ tay (nếu nó bị lệch)

# --- C. Góc Kẹp ---
GRIP_OPEN = 30
GRIP_CLOSE_BOX = 65

# --- D. Kết nối ---
SERIAL_PORT = "COM9"  # <--- Kiểm tra lại cổng COM
BAUDRATE = 9600


# =================================================================================
# 2. CLASS ĐIỀU KHIỂN ROBOT
# =================================================================================

class RobotArmPro:
    def __init__(self, port=SERIAL_PORT, baudrate=BAUDRATE):
        self.ser = None
        print(f"[INIT] 🔌 Connecting to {port}...")
        try:
            self.ser = serial.Serial(port, baudrate, timeout=1)
            time.sleep(2)  # Đợi Arduino khởi động
            print("[INIT] ✅ Connected!")
        except Exception as e:
            print(f"[INIT] ⚠️ Connection Failed. Running in SIMULATION mode.")

    def _send(self, b, s, e, w, g):
        """
        Gửi lệnh 5 thông số xuống Arduino
        Format: B:xx,S:xx,E:xx,W:xx,G:xx
        """
        # 1. Áp dụng Offset & Giới hạn an toàn
        final_b = max(0, min(180, b + BASE_OFFSET))
        final_s = max(10, min(150, s + SHOULDER_OFFSET))
        final_e = max(10, min(160, e + ELBOW_OFFSET))
        final_w = max(0, min(180, w + WRIST_OFFSET))  # Cổ tay thường quay 0-180

        # 2. Gửi lệnh
        cmd = f"B:{final_b:.1f},S:{final_s:.1f},E:{final_e:.1f},W:{final_w:.1f},G:{int(g)}\n"

        if self.ser:
            self.ser.write(cmd.encode())
        else:
            print(f"[SIM] 📤 Send: {cmd.strip()}")

    # =============================================================================
    # 3. THUẬT TOÁN 3 KHỚP (3-LINK IK) - "TRÁI TIM" CỦA ROBOT
    # =============================================================================
    def solve_ik_3dof(self, reach_r, height_y, alpha_deg):
        """
        Tính góc Vai, Khuỷu, Cổ tay.
        Input:
          - reach_r: Khoảng cách vươn xa (Horizontal distance)
          - height_y: Độ cao (Vertical height)
          - alpha_deg: Góc hướng kẹp (-90 là chúc xuống đất)
        """
        # Đổi góc kẹp ra radian
        alpha_rad = math.radians(alpha_deg)

        # --- BƯỚC 1: Tìm vị trí cổ tay (Wrist) ---
        wx = reach_r - L3 * math.cos(alpha_rad)
        wy = height_y - L3 * math.sin(alpha_rad)

        # --- BƯỚC 2: Giải bài toán 2 khâu (Vai -> Cổ tay) ---
        dist = math.sqrt(wx ** 2 + wy ** 2)

        # Check tầm với
        if dist > (L1 + L2):
            print(f"[IK] ⚠️ Unreachable! Dist={dist:.1f} > Max={L1 + L2}")
            return None

        # Định lý hàm số Cos
        a, b, c = L1, L2, dist
        try:
            # Góc Khuỷu
            cos_elbow = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
            cos_elbow = max(-1.0, min(1.0, cos_elbow))
            elbow_inside = math.degrees(math.acos(cos_elbow))
            elbow_angle = 180 - elbow_inside

            # Góc Vai
            cos_shoulder_tri = (a ** 2 + c ** 2 - b ** 2) / (2 * a * c)
            cos_shoulder_tri = max(-1.0, min(1.0, cos_shoulder_tri))
            angle_shoulder_tri = math.degrees(math.acos(cos_shoulder_tri))

            angle_elevation = math.degrees(math.atan2(wy, wx))
            shoulder_angle = angle_elevation + angle_shoulder_tri

            # --- BƯỚC 3: Tính góc Cổ tay ---
            # Góc cẳng tay so với đất = Shoulder - (180 - Elbow)
            # Góc kẹp mong muốn = Alpha
            # Wrist_Servo = Alpha - Forearm_Global + 180 (bù trừ)

            forearm_global = shoulder_angle - (180 - elbow_angle)
            wrist_angle = alpha_deg - forearm_global + 180

            return shoulder_angle, elbow_angle, wrist_angle

        except Exception as e:
            print(f"[IK] Error: {e}")
            return None

    # =============================================================================
    # 4. HÀM GẮP THÔNG MINH (SMART PICK)
    # =============================================================================
    def move_to(self, x, y, z, alpha=-90, grip=GRIP_OPEN, duration=1.0):
        """
        Di chuyển robot đến toạ độ (x, y, z) trong không gian 3D
        x: Trái/Phải
        y: Xa/Gần (Reach)
        z: Cao/Thấp (Height)
        alpha: Góc kẹp (-90: Chúc xuống, 0: Ngang)
        """
        # 1. Tính góc Đế (Base)
        if y == 0: y = 0.001
        base_angle = 90 - math.degrees(math.atan2(x, y))

        # 2. Tính tầm vươn (Reach) trên mặt phẳng ngang
        reach = math.sqrt(x ** 2 + y ** 2)

        # 3. Tính IK 3 khớp
        ik_result = self.solve_ik_3dof(reach, z, alpha)

        if ik_result:
            s, e, w = ik_result
            self._send(base_angle, s, e, w, grip)
            time.sleep(duration)
        else:
            print("[MOVE] ❌ Cannot reach target!")

    def pick_and_place(self, x_target, y_target):
        """
        Kịch bản: Gắp vật tại (x, y) trên mặt đất
        """
        print(f"\n[TASK] 🎯 Gắp vật tại X={x_target}, Y={y_target}")

        # 1. Về Home
        self.move_to(0, 10, 15, alpha=0, grip=GRIP_OPEN)

        # 2. Tiếp cận (Lơ lửng trên vật 10cm, kẹp chúc xuống -90 độ)
        print("[1] Approach...")
        self.move_to(x_target, y_target, z=10, alpha=-90, grip=GRIP_OPEN)

        # 3. Hạ cánh (Xuống z=2cm để gắp)
        print("[2] Descend...")
        self.move_to(x_target, y_target, z=2, alpha=-90, grip=GRIP_OPEN)

        # 4. Kẹp
        print("[3] Grip...")
        self.move_to(x_target, y_target, z=2, alpha=-90, grip=GRIP_CLOSE_BOX)

        # 5. Nhấc lên (Về độ cao 15cm)
        print("[4] Lift...")
        self.move_to(x_target, y_target, z=15, alpha=-90, grip=GRIP_CLOSE_BOX)

        # 6. Đi thả (Sang bên phải)
        print("[5] Place...")
        self.move_to(15, 0, 10, alpha=-45, grip=GRIP_CLOSE_BOX)  # Thả nghiêng -45 độ

        # 7. Nhả kẹp & Về Home
        print("[6] Release...")
        self.move_to(15, 0, 10, alpha=-45, grip=GRIP_OPEN)
        self.move_to(0, 10, 15, alpha=0, grip=GRIP_OPEN)
        print("[DONE] ✅ Mission Complete!")

    def close(self):
        if self.ser: self.ser.close()


# =================================================================================
# 5. MAIN
# =================================================================================
if __name__ == "__main__":
    bot = RobotArmPro()

    try:
        # Test: Gắp vật cách robot 15cm về phía trước
        bot.pick_and_place(x_target=0, y_target=15)

    except KeyboardInterrupt:
        print("\n[STOP] Dừng chương trình.")
    finally:
        bot.close()