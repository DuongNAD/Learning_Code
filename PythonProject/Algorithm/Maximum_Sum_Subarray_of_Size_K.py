array = [5, 9, 7, 3, 1, 4, 11, 2, 6]
n = len(array)
k =3
# Iterations = N - K + 1
# N là số phần tử của mảng
# K là số phần tử của cửa sổ trượt

max_sum =0
for i in range(n -k +1):
    current_window = array[i:i+k]
    current_total = sum(current_window)
    if max_sum < current_total:
        max_sum = current_total
        best_window = current_window

print(f"Tổng lớn nhất là: {max_sum}")
print(f"3 số đó là: {best_window}")
