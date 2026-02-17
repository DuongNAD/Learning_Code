import sys
import time
import random
import os
import shutil

# --- CONFIGURATION (Cấu hình) ---
BLUE = "\033[94m"
CYAN = "\033[96m"
GREEN = "\033[92m"
WHITE = "\033[97m"
RESET = "\033[0m"

BLOCK = "[]"  # Character to represent a block

# --- PIXEL MAP FOR "DK TEAM" ---
# 1 = Block, 0 = Empty Space
# Designed a clearer font 5x30
DK_MAP = [
    "11100100100011111011110010001010001",
    "10010101000000100010000101001101011",
    "10010110000000100011100111001010101",
    "10010101000000100010000101001000001",
    "11100100100000100011110100101000001"
]


def get_terminal_size():
    """Get current width and height of the terminal."""
    return shutil.get_terminal_size((80, 24))


def hide_cursor():
    sys.stdout.write("\033[?25l")


def show_cursor():
    sys.stdout.write("\033[?25h")


def move_cursor(row, col):
    """Move cursor to specific coordinate without clearing screen."""
    # Col * 2 because our block '[]' is 2 chars wide
    sys.stdout.write(f"\033[{row};{col * 2}H")


def draw_at(row, col, text, color=RESET):
    """Render a text at specific position."""
    move_cursor(row, col)
    sys.stdout.write(f"{color}{text}{RESET}")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def tetris_intro():
    clear_screen()
    hide_cursor()

    cols, rows = get_terminal_size()
    map_h = len(DK_MAP)
    map_w = len(DK_MAP[0])

    # Calculate offsets to center the text (Tính toán căn giữa)
    start_row = (rows - map_h) // 2 + 1
    # Adjust col calculation because each block is 2 chars wide
    start_col = (cols - (map_w * 2)) // 4 + 1

    if start_row < 1: start_row = 1
    if start_col < 1: start_col = 1

    # 1. Identify Target Coordinates (Xác định tọa độ đích)
    targets = []
    for r in range(map_h):
        for c in range(map_w):
            if DK_MAP[r][c] == '1':
                # Store dictionary of target row/col
                targets.append({
                    'target_r': start_row + r,
                    'target_c': start_col + c,
                    'color': BLUE  # Default color
                })

    # Randomize the falling order (Xáo trộn thứ tự rơi)
    random.shuffle(targets)

    # 2. Animation Loop (Vòng lặp hiệu ứng)
    # We drop blocks one by one
    for i, item in enumerate(targets):
        dest_r = item['target_r']
        dest_c = item['target_c']

        # Start falling from the very top
        # Acceleration logic: The closer to the end, the faster it falls to save time
        # Logic tăng tốc: Càng về sau rơi càng nhanh để đỡ tốn thời gian
        speed = 0.01 if i < 10 else 0.005
        if i > len(targets) * 0.7: speed = 0.002  # Super fast at the end

        for curr_r in range(1, dest_r + 1):
            # A. Erase previous position (Xóa vị trí cũ - Quan trọng!)
            if curr_r > 1:
                draw_at(curr_r - 1, dest_c, "  ")  # Overwrite with space

            # B. Draw current position (Vẽ vị trí mới)
            # Use CYAN for falling block, change to BLUE when landed
            color = CYAN if curr_r < dest_r else BLUE
            draw_at(curr_r, dest_c, BLOCK, color)

            sys.stdout.flush()

            # Sleep only if falling, no sleep on last frame to lock it instantly
            if curr_r < dest_r:
                time.sleep(speed)

    # 3. Final Flash Effect (Hiệu ứng nhấp nháy chốt hạ)
    # Highlight keywords: Flash, Loop, Color Cycle
    time.sleep(0.2)
    colors = [WHITE, CYAN, BLUE, GREEN, BLUE]

    for color in colors:
        for item in targets:
            draw_at(item['target_r'], item['target_c'], BLOCK, color)
        sys.stdout.flush()
        time.sleep(0.1)

    # Move cursor to bottom safe area
    move_cursor(rows, 1)
    print(f"\n{GREEN}>>> SYSTEM: DK TEAM ONLINE.{RESET}\n")
    show_cursor()


if __name__ == "__main__":
    try:
        tetris_intro()
    except KeyboardInterrupt:
        show_cursor()
        print("\n[!] Animation Cancelled.")