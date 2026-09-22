import math
import time
import serial

# =================================================================================
# 1. CONFIGURATION (CẤU HÌNH HỆ THỐNG)
# =================================================================================

# --- A. Physical Dimensions (Kích thước vật lý) ---
# Anh lấy thước đo chính xác khoảng cách giữa các tâm trục xoay nhé!
L1_SHOULDER_TO_ELBOW = 10.5  # Bắp tay
L2_FOREARM = 9.0  # Cẳng tay (đến cổ tay)
L3_HAND = 6.5  # Bàn tay (từ cổ tay ra đầu kẹp)

# [VIRTUAL LINK] Kỹ thuật "Cánh tay ảo"
# Ta coi Cẳng tay + Bàn tay là một thanh thẳng dài duy nhất để dễ tính toán
L2_EFFECTIVE = L2_FOREARM + L3_HAND

# --- B. Calibration & Offsets (Cân chỉnh sai số) ---
# Thay đổi số này nếu robot bị lệch
BASE_OFFSET = 0
SHOULDER_OFFSET = 15  # Nâng vai lên 15 độ (để bù trọng lực)
ELBOW_OFFSET = -10  # Gập khuỷu xuống

# --- C. Servo Angles (Góc Servo) ---
GRIP_OPEN = 30  # Mở
GRIP_CLOSE_BOX = 65  # Kẹp vừa
GRIP_CLOSE_FULL = 85  # Kẹp chặt

# --- D. Connection (Kết nối) ---
SERIAL_PORT = "COM9"  # <--- Anh kiểm tra lại đúng cổng COM nhé
BAUDRATE = 9600


# =================================================================================
# 2. THE ROBOT CONTROLLER CLASS
# =================================================================================

class RobotArmController:
    def __init__(self, port=SERIAL_PORT, baudrate=BAUDRATE):
        """
        Khởi tạo kết nối đến Robot
        """
        self.ser = None
        self.is_connected = False

        print(f"[INIT] 🔌 Connecting to robot at {port}...")
        try:
            self.ser = serial.Serial(port, baudrate, timeout=1)
            time.sleep(2)  # Waiting for Arduino reboot
            self.is_connected = True
            print(f"[INIT] ✅ Success! Robot is ready.")
        except Exception as e:
            print(f"[INIT] ⚠️ Connection Failed: {e}")
            print(f"[INIT] 🚀 Running in SIMULATION MODE (No hardware).")

    def _send_command(self, b, s, e, g):
        """
        Gửi lệnh xuống Arduino (Low-level communication)
        """
        # 1. Apply Offsets (Bù trừ sai số)
        final_b = b + BASE_OFFSET
        final_s = s + SHOULDER_OFFSET
        final_e = e + ELBOW_OFFSET

        # 2. Safety Clamps (Giới hạn an toàn)
        final_b = max(0, min(180, final_b))
        final_s = max(10, min(150, final_s))  # Không cho vai đập xuống đất
        final_e = max(10, min(150, final_e))  # Không cho khuỷu gập quá đà

        # 3. Send Data
        # Format: B:90,S:60,E:45,G:30
        cmd = f"B:{final_b:.1f},S:{final_s:.1f},E:{final_e:.1f},G:{int(g)}\n"

        if self.is_connected and self.ser:
            self.ser.write(cmd.encode())
            # time.sleep(0.05) # Optional: delay nhỏ để tránh nghẽn lệnh
        else:
            # In ra màn hình để debug khi không cắm robot
            print(f"[SIM] 🦾 Move -> Base:{final_b:.0f}° | Shldr:{final_s:.0f}° | Elbw:{final_e:.0f}° | Grip:{g}")

    def solve_ik(self, x_cm, z_cm):
        """
        INVERSE KINEMATICS (Động học ngược)
        Tính toán góc servo từ tọa độ (x, z) sử dụng L1 và L2_EFFECTIVE
        """
        # --- 1. Base Angle (Góc Đế) ---
        if z_cm == 0: z_cm = 0.001
        # atan2 trả về radian, ta đổi sang degree
        raw_rad = math.atan2(x_cm, z_cm)
        base_angle = 90 - math.degrees(raw_rad)

        # --- 2. Planar IK (Vai & Khuỷu) ---
        # Khoảng cách từ vai đến vật (Hypotenuse)
        dist = math.sqrt(x_cm ** 2 + z_cm ** 2)

        # Kiểm tra tầm với (Reach Limit)
        max_reach = L1_SHOULDER_TO_ELBOW + L2_EFFECTIVE
        if dist > max_reach:
            print(f"[MATH] ⚠️ Target unreachable! ({dist:.1f}cm > {max_reach:.1f}cm)")
            return base_angle, 45, 45  # Trả về góc an toàn

        # Định lý hàm số Cos (Law of Cosines)
        # a, b, c tương ứng với các cạnh tam giác
        a = L1_SHOULDER_TO_ELBOW
        b = L2_EFFECTIVE  # Dùng cánh tay ảo (đã cộng gộp)
        c = dist

        try:
            # Tính góc Khuỷu (Elbow)
            cos_elbow = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
            cos_elbow = max(-1.0, min(1.0, cos_elbow))  # Clip value to range [-1, 1]
            elbow_angle_inside = math.degrees(math.acos(cos_elbow))
            elbow_angle = 180 - elbow_angle_inside

            # Tính góc Vai (Shoulder)
            cos_shoulder = (a ** 2 + c ** 2 - b ** 2) / (2 * a * c)
            cos_shoulder = max(-1.0, min(1.0, cos_shoulder))
            shoulder_angle = math.degrees(math.acos(cos_shoulder))

            return base_angle, shoulder_angle, elbow_angle

        except ValueError:
            print("[MATH] ❌ Calculation Error")
            return 90, 90, 90

    # =============================================================================
    # 3. HIGH-LEVEL ACTIONS (CÁC HÀNH ĐỘNG CẤP CAO)
    # =============================================================================

    def move_to_home(self):
        """Về vị trí nghỉ"""
        print("[ACTION] 🏠 Going Home")
        self._send_command(90, 80, 30, GRIP_OPEN)
        time.sleep(1.5)

    def pick_item(self, x, z):
        """
        Quy trình gắp vật tại tọa độ (x, z)
        """
        print(f"\n[TASK] 🎯 Start Picking at X={x}, Z={z}")

        # 1. Tính toán góc
        b, s, e = self.solve_ik(x, z)
        print(f"[MATH] Solution -> B:{b:.1f}, S:{s:.1f}, E:{e:.1f}")

        # 2. Tiếp cận (Approach)
        # Đi đến vị trí phía trên vật một chút để tránh va chạm
        self._send_command(b, s - 15, e, GRIP_OPEN)
        time.sleep(1.0)

        # 3. Hạ xuống (Descend)
        self._send_command(b, s, e, GRIP_OPEN)
        time.sleep(1.5)  # Đợi robot dừng hẳn rung lắc

        # 4. Kẹp (Grasp)
        print("[ACTION] 🤏 Gripping...")
        self._send_command(b, s, e, GRIP_CLOSE_BOX)
        time.sleep(0.8)

        # 5. Nhấc lên (Lift)
        print("[ACTION] 🔼 Lifting...")
        # Giữ nguyên khuỷu, giảm góc vai để nhấc lên cao
        self._send_command(b, s - 30, e, GRIP_CLOSE_BOX)
        time.sleep(1.0)

        print("[TASK] ✅ Picked successfully!")

    def place_item(self, x_drop=15, z_drop=0):  # Mặc định thả bên phải
        """
        Quy trình thả vật
        """
        print(f"[TASK] 🔄 Placing at X={x_drop}, Z={z_drop}")

        # 1. Quay sang chỗ thả
        b, s, e = self.solve_ik(x_drop, z_drop)
        self._send_command(b, s - 20, e, GRIP_CLOSE_BOX)  # Di chuyển ở độ cao an toàn
        time.sleep(2.0)

        # 2. Hạ xuống
        self._send_command(b, s, e, GRIP_CLOSE_BOX)
        time.sleep(1.0)

        # 3. Mở kẹp
        print("[ACTION] 🖐️ Releasing...")
        self._send_command(b, s, e, GRIP_OPEN)
        time.sleep(0.5)

        # 4. Về nhà
        self.move_to_home()

    def close(self):
        if self.ser and self.is_connected:
            self.ser.close()
            print("[EXIT] Serial connection closed.")


# =================================================================================
# 4. MAIN PROGRAM (CHƯƠNG TRÌNH CHÍNH)
# =================================================================================

if __name__ == "__main__":
    # Khởi tạo robot
    robot = RobotArmController()

    try:
        # --- TEST CASE 1: Gắp vật ở xa ---
        # Giả sử vật cách tâm 15cm về phía trước
        robot.pick_item(x=0, z=15)
        robot.place_item()  # Thả sang bên phải

        # --- TEST CASE 2: Gắp vật ở gần ---
        # robot.pick_item(x=5, z=10)
        # robot.place_item()

    except KeyboardInterrupt:
        print("\n[STOP] 🛑 User stopped program.")
    finally:
        robot.close()