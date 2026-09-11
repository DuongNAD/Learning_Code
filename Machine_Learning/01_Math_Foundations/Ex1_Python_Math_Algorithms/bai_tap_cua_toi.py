# ==============================================================================
# 📝 NƠI BẠN TỰ TAY GÕ CODE THỰC HÀNH (BẮT ĐẦU TỪ DỄ ĐẾN KHÓ)
# ==============================================================================
# Mẹo: Gõ xong bạn bấm nút Play (▶) ở góc trên bên phải để xem kết quả nhé!
# ==============================================================================

# ------------------------------------------------------------------------------
# 🟢 THỬ THÁCH 1: TÁCH SỐ ÂM VÀ SỐ DƯƠNG
# ------------------------------------------------------------------------------
# Cho danh sách các số sau:
danh_sach = [-5, 12, -3, 8, -1, 0, 7]

# 1. Tạo 2 rổ rỗng để đựng:
so_am = []
so_duong = []

# 2. Bạn hãy thử tự viết vòng for và if-else dưới đây nhé:
# (Gợi ý: for x in danh_sach: ...)

# 👉 BẠN HÃY GÕ CODE CỦA BẠN Ở ĐÂY:
for i in danh_sach:
    if i < 0:
        so_am.append(i)
    else:
        so_duong.append(i)



# 3. In kết quả ra xem
print("Danh sách ban đầu:", danh_sach)
print("Số âm thu được:", so_am)
print("Số dương thu được:", so_duong)
