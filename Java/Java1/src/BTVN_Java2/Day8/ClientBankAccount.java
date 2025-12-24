package BTVN_Java2.Day8;

public class ClientBankAccount {
    public static void main(String[] args) {
    BankAccount newAccount = new BankAccount
            .BankAccountBuilder("GP Coder", "0123456789")
            .withEmail("contact@gpcoder.com")
            .wantNewsletter(true)
            .build();
    System.out.println(newAccount);
}
}
