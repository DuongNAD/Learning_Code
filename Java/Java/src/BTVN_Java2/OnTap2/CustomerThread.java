package BTVN_Java2.OnTap2;

public class CustomerThread extends Thread {
    private TicketCounter ticketCounter;
    private String customerName;

    public CustomerThread(TicketCounter ticketCounter, String customerName) {
        this.ticketCounter = ticketCounter;
        this.customerName = customerName;
    }
    @Override
    public void run() {
        ticketCounter.buyTicket(customerName);
    }
}
