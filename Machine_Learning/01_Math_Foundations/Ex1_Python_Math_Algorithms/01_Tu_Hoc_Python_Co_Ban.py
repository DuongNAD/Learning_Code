# ==============================================================================
# 🎯 TỰ HỌC PYTHON TỪ CƠ BẢN ĐẾN NÂNG CAO (KHÔNG CẦN CODE PHỨC TẠP)
# ==============================================================================
# File này viết theo phong cách đơn giản nhất:
# Dễ hiểu - Dễ nhìn - Chạy thử được ngay từng bài
# ==============================================================================

# ------------------------------------------------------------------------------
# 🟢 BÀI 1: TÁCH SỐ ÂM VÀ SỐ DƯƠNG
# Ý tưởng: Có 1 rổ số, nhặt số âm bỏ vào rổ âm, số dương bỏ vào rổ dương.
# ------------------------------------------------------------------------------
print("=== BÀI 1: TÁCH SỐ ÂM & DƯƠNG ===")

# 1. Danh sách số ban đầu
danh_sach_so = [-10, 25, -4, 0, 15, -8, 30]

# 2. Tạo 2 cái rổ rỗng để chứa
so_am = []
so_duong = []

# 3. Duyệt qua từng số (dùng vòng for đơn giản)
for so in danh_sach_so:
    if so < 0:
        so_am.append(so)      # Nhét vào rổ số âm
    else:
        so_duong.append(so)   # Nhét vào rổ số dương

# 4. In kết quả xem
print("Danh sách gốc:", danh_sach_so)
print("-> Các số âm:", so_am)
print("-> Các số dương (kèm số 0):", so_duong)
print()


# ------------------------------------------------------------------------------
# 🟢 BÀI 2: ĐẾM XEM SỐ NÀO XUẤT HIỆN NHIỀU LẦN
# Ý tưởng: Đếm số lần xuất hiện bằng hàm có sẵn danh_sach.count(so)
# ------------------------------------------------------------------------------
print("=== BÀI 2: ĐẾM SỐ LẦN XUẤT HIỆN ===")

# Danh sách có nhiều số bị lặp lại
cac_so = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
nguong_k = 3  # Muốn tìm số xuất hiện nhiều hơn 3 lần

so_xuat_hien_nhieu = []

for so in cac_so:
    # Nếu số lần xuất hiện > 3 VÀ chưa có trong kết quả thì thêm vào
    if cac_so.count(so) > nguong_k and so not in so_xuat_hien_nhieu:
        so_xuat_hien_nhieu.append(so)

print("Dữ liệu:", cac_so)
print(f"-> Các số xuất hiện nhiều hơn {nguong_k} lần là:", so_xuat_hien_nhieu)
print()


# ------------------------------------------------------------------------------
# 🟢 BÀI 3: DUYỆT 2 SỐ LIỀN KỀ NHAU (CỬA SỔ TRƯỢT)
# Ý tưởng: Lấy từng cặp (số đứng trước, số đứng sau)
# ------------------------------------------------------------------------------
print("=== BÀI 3: LẤY CẶP SỐ LIỀN KỀ ===")

mang_so = [10, 20, 30, 40, 50]

print("Duyệt từng cặp liền kề:")
for i in range(len(mang_so) - 1):
    so_truoc = mang_so[i]
    so_sau = mang_so[i + 1]
    print(f"  Cặp {i+1}: ({so_truoc}, {so_sau}) -> Tổng = {so_truoc + so_sau}")

print("\n🎉 XONG 3 BÀI CƠ BẢN NHẤT! BẠN HÃY CHẠY THỬ XEM KẾT QUẢ NHÉ!")
