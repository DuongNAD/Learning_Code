package Day4;

public abstract class NhanVien {
    protected String hoTen;
    protected double luong;

    public NhanVien(String hoTen, double luong) {
        this.hoTen = hoTen;
        this.luong = luong;
    }

    public abstract double getLuong();

    public void output() {
        System.out.println("Họ và tên: " + hoTen);
        System.out.println("Luong co ban: " + luong);
    }
}
