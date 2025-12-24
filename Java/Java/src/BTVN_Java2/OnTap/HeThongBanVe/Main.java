package BTVN_Java2.OnTap.HeThongBanVe;

public class Main {
    public static void main(String[] args) {
        TicketBooth tb = new TicketBooth();

        System.out.println("Hệ thống bán vé");

        for (int i =0;i<15;i++){
            Customer customer = new Customer(tb, "Khách hàng " + (i+1) );
            customer.start();
        }
    }
}