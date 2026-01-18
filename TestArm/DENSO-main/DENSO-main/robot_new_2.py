import serial
import time
import math

# =============================================================================
# 1. CẤU HÌNH KÍCH THƯỚC ROBOT (CẦN ĐO THỰC TẾ)
# =============================================================================

# [SỬA Ở ĐÂY 1]: Đo đoạn bắp tay (cm) - Từ tâm ốc Vai đến tâm ốc Khuỷu
L1 = 10.5   

# [SỬA Ở ĐÂY 2]: Đo đoạn cẳng tay + kẹp (cm) - Từ tâm ốc Khuỷu đến đầu kẹp
L2_TOTAL = 22.0 

# [SỬA Ở ĐÂY 3]: Chiều cao từ MẶT BÀN lên TÂM ỐC VAI (cm)
# Đây là đoạn thẳng đứng từ bàn lên tâm xoay.
BASE_HEIGHT_FROM_TABLE = 8.5 # Đo từ mặt bàn đến tâm xoay thứ 2

# [SỬA Ở ĐÂY 4]: Tinh chỉnh sai số lắp đặt (Calibration)
# Nếu robot bị lệch thì sửa số ở đây (+ hoặc - độ)
OFFSET_BASE     = 0 # Lệch trái phải (Trái - Giảm  && Phải - Tăng)
OFFSET_SHOULDER = 0 # Nếu gắp non - Giảm && gắp quá - Tăng
OFFSET_ELBOW    = 0

class RobotArm:
    def __init__(self, port="COM9", baudrate=9600):
        self.ser = None
        # Lưu vị trí hiện tại của các khớp để tính toán đường đi mượt
        self.cur_b = 90
        self.cur_s = 90
        self.cur_e = 90
        
        try:
            self.ser = serial.Serial(port, baudrate, timeout=1)
            time.sleep(2) 
            print(f"[ROBOT] ✅ Connected to {port}")
        except Exception as e:
            print(f"[ROBOT] ⚠️ Error: {e}")
            print("[ROBOT] 🚀 Simulation Mode")

    def send_cmd(self, b, s, e, g):
        """ Gửi lệnh xuống Arduino """
        # Áp dụng offset và giới hạn góc (0-180)
        b = max(0, min(180, int(b + OFFSET_BASE)))
        s = max(0, min(180, int(s + OFFSET_SHOULDER)))
        e = max(0, min(180, int(e + OFFSET_ELBOW)))
        g = max(10, min(100, int(g)))
        
        cmd = f"B:{b},S:{s},E:{e},G:{g}\n"
        if self.ser:
            self.ser.write(cmd.encode())
            # Nghỉ rất ngắn để tránh nghẽn lệnh ở baudrate 9600
            time.sleep(0.02)
        else:
            print(f"[SIM] {cmd.strip()}")

    def inverse_kinematics(self, x, y, z_table):
        """
        Tính góc IK.
        x: Tọa độ ngang (Side)
        y: Tọa độ vươn xa (Reach) - Ứng với Z trong hệ trục trên giấy
        z_table: Độ cao so với mặt bàn - Ứng với Y trong hệ trục trên giấy
        """
        # --- QUAN TRỌNG: CHUYỂN ĐỔI HỆ TRỤC CHIỀU CAO ---
        # Hệ trục Robot lấy Vai làm gốc 0.
        # Hệ trục Bàn lấy Bàn làm gốc 0.
        # Công thức: Z_Robot = Z_Bàn - Chiều_Cao_Vai
        z_robot = z_table - BASE_HEIGHT_FROM_TABLE

        # 1. Tính góc Đế
        if y == 0: y = 0.001
        base_angle_rad = math.atan2(x, y)
        final_base = 90 - math.degrees(base_angle_rad)

        # 2. Tính toán 2D (Side View)
        r_ground = math.sqrt(x**2 + y**2)
        D = math.sqrt(r_ground**2 + z_robot**2)

        # Kiểm tra tầm với
        if D > (L1 + L2_TOTAL):
            print(f"[IK] ⚠️ Xa quá không với tới! Dist={D:.1f} > Max={L1+L2_TOTAL}")
            return None

        # 3. Định lý Cosin tính góc
        cos_elbow = (L1**2 + L2_TOTAL**2 - D**2) / (2 * L1 * L2_TOTAL)
        cos_elbow = max(-1.0, min(1.0, cos_elbow))
        elbow_rad = math.acos(cos_elbow)
        
        final_elbow = 180 - math.degrees(elbow_rad) # Servo khuỷu thường tính bù

        alpha = math.atan2(z_robot, r_ground)
        beta = math.acos((L1**2 + D**2 - L2_TOTAL**2) / (2 * L1 * D))
        final_shoulder = math.degrees(alpha + beta)

        return final_base, final_shoulder, final_elbow

    def move_to(self, x, y, z_table, g=30, steps=10):
        """ 
        Di chuyển đến tọa độ (x,y) và độ cao z_table (cm) 
        steps: Số bước chia nhỏ để làm mượt chuyển động (Càng lớn càng chậm & mượt)
        """
        angles = self.inverse_kinematics(x, y, z_table)
        if angles:
            tgt_b, tgt_s, tgt_e = angles
            
            # Nếu steps <= 1 thì chạy ngay lập tức (Logic cũ)
            if steps <= 1:
                self.send_cmd(tgt_b, tgt_s, tgt_e, g)
                self.cur_b, self.cur_s, self.cur_e = tgt_b, tgt_s, tgt_e
                return True

            # --- LOGIC CHIA NHỎ BƯỚC ĐI (SMOOTHING) ---
            diff_b = (tgt_b - self.cur_b) / steps
            diff_s = (tgt_s - self.cur_s) / steps
            diff_e = (tgt_e - self.cur_e) / steps

            for i in range(1, steps + 1):
                temp_b = self.cur_b + diff_b * i
                temp_s = self.cur_s + diff_s * i
                temp_e = self.cur_e + diff_e * i
                
                self.send_cmd(temp_b, temp_s, temp_e, g)
                
                # Thời gian nghỉ giữa các bước nhỏ (Tăng lên nếu muốn chậm hơn nữa)
                time.sleep(0.03) 

            # Cập nhật vị trí hiện tại
            self.cur_b = tgt_b
            self.cur_s = tgt_s
            self.cur_e = tgt_e
            
            # In ra để debug xem nó tính ra góc bao nhiêu
            print(f"[MOVE] TGT: X{x:.1f} Z(Reach){y:.1f} Y(Height){z_table} -> ANG: {tgt_b:.0f},{tgt_s:.0f},{tgt_e:.0f}")
            return True
        return False

    def close(self):
        if self.ser: self.ser.close()