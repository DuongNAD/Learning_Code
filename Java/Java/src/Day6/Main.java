package Day6;

// Lớp này là "người thợ" chỉ chứa các công cụ tính toán
class TienIchToanHoc {
    public static int cong(int a, int b) {
        System.out.println("-> Đang thực hiện phương thức cong()...");
        return a + b;
    }

    public static void inTong(int a, int b) {
        System.out.println("Bắt đầu thực hiện phương thức inTong()...");
        // Gọi phương thức static khác trong cùng lớp
        int ketQua = cong(a, b);
        System.out.println("Tổng là: " + ketQua);
    }
}

// Lớp này là "người quản lý" và chứa "cửa chính" của chương trình
public class Main {
    public static void main(String[] args) {
        // Người quản lý gọi người thợ làm việc
        // Vì các phương thức là static, ta gọi qua tên lớp TienIchToanHoc
        TienIchToanHoc.inTong(10, 5);
    }
}