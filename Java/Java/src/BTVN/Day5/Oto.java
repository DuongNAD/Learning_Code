package BTVN.Day5;

public class Oto extends PhuongTienGiaoThong {
    private int soChoNgoi;
    private String kieuDongCo;

    public Oto(String soXe, String nhaSanXuat, int namSanXuat, String mauXe, ChuXe chuXe, int soChoNgoi, String kieuDongCo) {
        super(soXe, nhaSanXuat, namSanXuat, mauXe, chuXe);
        this.soChoNgoi = soChoNgoi;
        this.kieuDongCo = kieuDongCo;
    }
    public int getSoChoNgoi() {
        return soChoNgoi;
    }
    public void setSoChoNgoi(int soChoNgoi) {
        this.soChoNgoi = soChoNgoi;
    }

    public String getKieuDongCo() {
        return kieuDongCo;
    }
    public void setKieuDongCo(String kieuDongCo){
        this.kieuDongCo = kieuDongCo;
    }

    @Override
    public void hienThiThongTin() {
        System.out.println("--- THÔNG TIN Ô TÔ ---");
        System.out.println("Số xe: " + getSoXe());
        System.out.println("Nhà sản xuất: " + getNhaSanXuat());
        System.out.println("Năm sản xuất: " + getNamSanXuat());
        System.out.println("Màu xe: " + getMauXe());
        System.out.println("Số chỗ ngồi: " + soChoNgoi);
        System.out.println("Kiểu động cơ: " + kieuDongCo);
        System.out.println("Chủ xe: " + getChuXe());
        System.out.println("----------------------");
    }
}
