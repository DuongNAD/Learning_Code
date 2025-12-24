package BTVN_Java2.OnTap.HeThongBanVe;

public class TicketBooth {
    private int availableTickets = 10;

    public synchronized void  sellTicket(String customerName){
        if(availableTickets > 0){
            System.out.println(customerName + " Đang thực hiện giao dịch");

            try{
                Thread.sleep(1000);
            }
            catch (InterruptedException e) {
                throw new RuntimeException(e);
            }

            availableTickets--;
            System.out.println("Đã mua vé thành công");
        }
        else {
            System.out.println(customerName + " - Đã hết vé");
        }
    }
}
