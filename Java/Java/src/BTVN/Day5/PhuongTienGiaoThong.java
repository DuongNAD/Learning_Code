package BTVN.Day5;

public abstract class PhuongTienGiaoThong {
    private String soXe;
    private String nhaSanXuat;
    private int namSanXuat;
    private String mauXe;
    private ChuXe chuXe;

    public PhuongTienGiaoThong(String soXe, String nhaSanXuat, int namSanXuat, String mauXe, ChuXe chuXe) {
        this.soXe = this.soXe;
        this.nhaSanXuat = this.nhaSanXuat;
        this.namSanXuat = this.namSanXuat;
        this.mauXe = this.mauXe;
        this.chuXe = this.chuXe;
    }

    public String getSoXe() {
        return soXe;
    }
    public void setSoXe(String soXe) {
        this.soXe = soXe;
    }
    public String getNhaSanXuat() {
        return nhaSanXuat;
    }
    public void setNhaSanXuat(String nhaSanXuat) {
        this.nhaSanXuat = nhaSanXuat;
    }
    public int getNamSanXuat() {
        return namSanXuat;
    }

    public void setNamSanXuat(int namSanXuat) {
        this.namSanXuat = namSanXuat;
    }
    public String getMauXe() {
        return mauXe;
    }
    public void setMauXe(String mauXe) {
        this.mauXe = mauXe;
    }
    public ChuXe getChuXe() {
        return chuXe;
    }
    public void setChuXe(ChuXe chuXe) {
        this.chuXe = chuXe;
    }

    public abstract void hienThiThongTin();

}
