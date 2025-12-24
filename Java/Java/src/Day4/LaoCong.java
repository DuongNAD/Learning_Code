package Day4;

public class LaoCong extends NhanVien {
    private int soGioLam;

    public LaoCong(String hoTen, double luong, int soGioLam) {
        super(hoTen, luong);
        this.soGioLam = soGioLam;
    }

    @Override
    public double getLuong() {
        return this.luong * this.soGioLam;
    }
}
