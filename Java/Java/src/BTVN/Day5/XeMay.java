package BTVN.Day5;

public class XeMay extends PhuongTienGiaoThong {
    private int congSuat;

    public XeMay(String soXe, String nhaSanXuat, int namSanXuat, String mauXe, ChuXe chuXe, int congSuat) {
        super(soXe, nhaSanXuat,namSanXuat, mauXe, chuXe);
        this.congSuat = congSuat;
    }

    public int getCongSuat() {
        return congSuat;
    }
    public void setCongSuat(int congSuat) {
        this.congSuat = congSuat;
    }

    @Override
    public void hienThiThongTin() {
        System.out.println("--- THÔNG TIN XE MÁY ---");
        System.out.println("Số xe: " + getSoXe());
        System.out.println("Nhà sản xuất: " + getNhaSanXuat());
        System.out.println("Năn sản xuất: " + getNamSanXuat());
        System.out.println("Màu xe: " + getMauXe());
        System.out.println("Công suất (CC): " + congSuat);
        System.out.println("Chủ xe: " + getChuXe());
        System.out.println("------------------------");
    }
}
