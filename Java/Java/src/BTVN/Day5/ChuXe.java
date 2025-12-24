package BTVN.Day5;

public class ChuXe {
    private String soCCCD;
    private String hoTen;
    private String email;

    public ChuXe(String soCCCD, String hoTen, String email) {
        this.soCCCD = soCCCD;
        this.hoTen = hoTen;
        this.email = email;
    }

    public String getSoCCCD() {
        return soCCCD;
    }
    public String getHoTen() {
        return hoTen;
    }
    public String getEmail() {
        return email;
    }

    @Override
    public String toString() {
        return "Số CMND: " + soCCCD + ", Họ tên: " + hoTen + ", Email: " + email;
    }

}
