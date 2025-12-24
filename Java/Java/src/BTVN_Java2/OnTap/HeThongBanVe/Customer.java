package BTVN_Java2.OnTap.HeThongBanVe;

public class Customer extends Thread{
    private TicketBooth booth;
    private String customerName;

    public Customer(TicketBooth booth, String customerName) {
        this.booth = booth;
        this.customerName = customerName;
    }
    public TicketBooth getBooth() {
        return booth;
    }
    public void setBooth(TicketBooth booth) {
        this.booth = booth;
    }
    public String getCustomerName() {
        return customerName;
    }
    public void setCustomerName(String customerName) {
        this.customerName = customerName;
    }
    @Override
    public void run() {
        booth.sellTicket(customerName);
    }
}
