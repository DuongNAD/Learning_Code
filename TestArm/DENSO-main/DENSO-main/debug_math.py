from robot_new_2 import RobotArmController
import time

print("[TEST] Đang kết nối Robot...")
robot = RobotArmController(port="COM9", baudrate=9600)

print("\n--- KIỂM TRA ĐIỀU KHIỂN ROBOT (HARDWARE TEST) ---")

print("1. Về vị trí Home...")
robot.move_home()
time.sleep(2)

print("2. Thử gắp tại vị trí X=0 (giữa), Z=12 (gần)...")
robot.pick_and_place(0, 12)

print("3. Thử gắp bên phải X=10, Z=12...")
robot.pick_and_place(10, 12)

print("\n[DONE] Hoàn tất bài test! Nếu robot múa may quay cuồng là OK.")