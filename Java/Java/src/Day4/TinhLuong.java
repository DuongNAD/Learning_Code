package Day4;

public class TinhLuong {
    public static void main(String[] args) {
        TruongPhong tp = new TruongPhong("Nguyễn Văn An", 3000, 500);
        System.out.println("--- THÔNG TIN TRƯỞNG PHÒNG ---");
        tp.output(); // Gọi phương thức của lớp cha
        System.out.printf("Tổng thu nhập: %.2f\n", tp.getLuong()); // Gọi phương thức đã được ghi đè

        System.out.println("\n--------------------------------\n");

        // Tạo một đối tượng Lao công
        LaoCong lc = new LaoCong("Trần Thị Bình", 15, 200); // Lương 15/giờ, làm 200 giờ
        System.out.println("--- THÔNG TIN LAO CÔNG ---");
        lc.output();
        System.out.printf("Tổng thu nhập: %.2f\n", lc.getLuong());
    }
}
