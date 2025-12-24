package BTVN.Day5;

public class XeTai extends PhuongTienGiaoThong {
    private double trongTai;

    public XeTai(String soXe, String nhaSanXuat, int namSanXuat, String mauXe, ChuXe chuXe, double trongTai) {
        super(soXe, nhaSanXuat, namSanXuat, mauXe, chuXe);
        this.trongTai = trongTai;
    }

    public double getTrongTai() {
        return trongTai;
    }
    public void setTrongTai(double trongTai) {
        this.trongTai = trongTai;
    }

    @Override
    public void hienThiThongTin() {
        System.out.println("--- THÔNG TIN XE TẢI ---");
        System.out.println("Số xe: " + getSoXe());
        System.out.println("Nhà sản xuất: " + getNhaSanXuat());
        System.out.println("Năm sản xuất: " + getNamSanXuat());
        System.out.println("Màu xe: " + getMauXe());
        System.out.println("Trọng tải (tấn): " + trongTai);
        System.out.println("Chủ xe: " + getChuXe().toString());
        System.out.println("-----------------------");
    }
}
