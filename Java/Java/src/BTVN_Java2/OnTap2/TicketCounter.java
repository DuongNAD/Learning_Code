package BTVN_Java2.OnTap2;

public class TicketCounter{
    private int numberOfTicket;

    TicketCounter(int numberOfTicket){
        this.numberOfTicket = numberOfTicket;
    }

    public synchronized void buyTicket(String customerName){
        if(this.numberOfTicket > 0){
            numberOfTicket--;
            System.out.println(customerName + " buy ticket success");
        }
        else{
            System.out.println("Customer "+customerName+" has been busy");
        }
    }
}
