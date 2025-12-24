package BTVN_Java2.OnTap2;

public class Main {
    public static void main(String[] args) {
        TicketCounter ticketCounter = new TicketCounter(10);
        for (int i = 0;i<15;i++){
            new CustomerThread(ticketCounter, "Customer " + (i+1)).start();
        }
    }
}
