package Day4;

public class TruongPhong extends NhanVien {
    private double trachNhiem;

    public TruongPhong(String hoTen, double luong, double trachNhiem) {
        super(hoTen, luong);
        this.trachNhiem = trachNhiem;
    }

    @Override
    public double getLuong() {
        return this.luong + this.trachNhiem;
    }
}
