package de_quy;

/**
 * Lớp này demo việc dùng đệ quy để tìm mức lương cao nhất
 * (giá trị lớn nhất) trong một mảng số nguyên.
 */
public class DeQuyMxLuong {

    /**
     * Hàm đệ quy tìm giá trị lớn nhất trong n phần tử đầu tiên của mảng.
     *
     * @param luong Mảng chứa các mức lương (int)
     * @param n     Số lượng phần tử cần xét (tính từ đầu mảng, ví dụ: n=4 là
     * xét 4 phần tử đầu tiên)
     * @return Mức lương cao nhất trong n phần tử đó
     */
    public static int findMaxLuong(int[] luong, int n) {
        // --- TRƯỜNG HỢP CƠ SỞ (BASE CASE) ---
        // (dòng 8)
        // Nếu chỉ xét 1 phần tử (n == 1),
        // thì phần tử đó (luong[0]) chính là lớn nhất.
        if (n == 1) {
            return luong[0];
        }

        // --- TRƯỜNG HỢP ĐỆ QUY (RECURSIVE CASE) ---
        // (dòng 10)
        // 1. Giả sử ta đã biết Lương Cao Nhất của (n-1) phần tử đầu tiên.
        //    Gọi đệ quy để tìm giá trị đó.
        int maxOfRest = findMaxLuong(luong, n - 1);

        // (dòng 11)
        // 2. Bây giờ, ta chỉ cần so sánh `maxOfRest`
        //    với phần tử cuối cùng (thứ n, index là n-1).
        //    Giá trị nào lớn hơn thì đó là kết quả của n phần tử.
        return Math.max(luong[n - 1], maxOfRest);
    }

    public static void main(String[] args) {
        // (dòng 15)
        // Ví dụ mảng lương
        int[] luong = {5000, 7000, 9000, 6000};

        // (dòng 16)
        // Bắt đầu tìm với toàn bộ mảng (số phần tử = luong.length)
        int maxLuong = findMaxLuong(luong, luong.length);

        // (dòng 17)
        // In kết quả
        System.out.println("Luong cao nhat trong cong ty la: " + maxLuong);
    }
}