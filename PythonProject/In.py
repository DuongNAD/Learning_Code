import numpy as np
import matplotlib.pyplot as plt

# --- 1. System Configuration (Cấu hình hệ thống) ---
L1 = 1.0  # Length of link 1 (Độ dài cánh tay trên)
L2 = 1.0  # Length of link 2 (Độ dài cẳng tay)


def inverse_kinematics(x, y):
    """
    Input: Target coordinates (x, y)
    Output: Joint angles (theta1, theta2) in radians
    """
    # Calculate distance from base to target (Khoảng cách từ gốc đến đích)
    r = np.sqrt(x ** 2 + y ** 2)

    # Workspace Check: Kiểm tra xem vật có nằm ngoài tầm với không
    if r > (L1 + L2):
        print("Target is unreachable! (Vượt quá tầm với)")
        return None, None

    # --- 2. Algorithm Core (Lõi thuật toán) ---
    # Using Law of Cosines to find Theta 2 (Góc khuỷu tay)
    # Cosine Rule: c^2 = a^2 + b^2 - 2ab*cos(C)
    cos_theta2 = (x ** 2 + y ** 2 - L1 ** 2 - L2 ** 2) / (2 * L1 * L2)

    # Calculate theta2 (Inverse Cosine)
    theta2 = np.arccos(cos_theta2)  # Elbow UP solution

    # Calculate Theta 1 (Góc vai)
    # Beta is the angle between the line connecting base-target and link 1
    k1 = L1 + L2 * np.cos(theta2)
    k2 = L2 * np.sin(theta2)
    theta1 = np.arctan2(y, x) - np.arctan2(k2, k1)

    return theta1, theta2


def plot_robot_arm(theta1, theta2, target_x, target_y):
    """
    Visualization function (Hàm hiển thị mô phỏng)
    """
    # Coordinates of Joint 1 (Base - Gốc)
    x0, y0 = 0, 0

    # Coordinates of Joint 2 (Elbow - Khuỷu)
    x1 = L1 * np.cos(theta1)
    y1 = L1 * np.sin(theta1)

    # Coordinates of End-effector (Hand - Bàn kẹp)
    x2 = x1 + L2 * np.cos(theta1 + theta2)
    y2 = y1 + L2 * np.sin(theta1 + theta2)

    # Setup plot
    plt.figure(figsize=(6, 6))

    # Draw links (Vẽ cánh tay)
    plt.plot([x0, x1], [y0, y1], 'b-o', linewidth=5, label='Link 1')  # Blue line
    plt.plot([x1, x2], [y1, y2], 'r-o', linewidth=5, label='Link 2')  # Red line

    # Draw target (Vẽ điểm đích)
    plt.plot(target_x, target_y, 'g*', markersize=15, label='Target Object')

    # Settings
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.grid(True)
    plt.title(f"Simulation: Reach ({target_x}, {target_y})")
    plt.legend()
    plt.show()


# --- 3. Run Simulation (Chạy thử) ---
# Anh Dương thử đổi tọa độ ở đây nhé:
target_x = 1.2
target_y = 0.8

t1, t2 = inverse_kinematics(target_x, target_y)

if t1 is not None:
    print(f"Calculated Angles (Radian): Theta1 = {t1:.2f}, Theta2 = {t2:.2f}")
    print(f"Calculated Angles (Degree): Theta1 = {np.degrees(t1):.2f}, Theta2 = {np.degrees(t2):.2f}")
    plot_robot_arm(t1, t2, target_x, target_y)