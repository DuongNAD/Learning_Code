package BTVN_Java2.Day8;

public class BankAccount {
    private final String name;
    private final String accountNumber;
    private final String address;
    private final String email;
    private final boolean newsLetter;
    private final boolean moblieBanking;

    public BankAccount(String name, String accountNumber, String address, String email, boolean newsLetter, boolean moblieBanking) {
        this.name = name;
        this.accountNumber = accountNumber;
        this.address = address;
        this.email = email;
        this.newsLetter = newsLetter;
        this.moblieBanking = moblieBanking;
    }

    public static class BankAccountBuilder {
        private String name;
        private String accountNumber;
        private String address;
        private String email;
        private boolean newsletter;
        private boolean mobileBanking;

        public BankAccountBuilder(String name, String  accountNumber) {
            this.name = name;
            this.accountNumber = accountNumber;
        }

        public BankAccountBuilder withAddress(String address) {
            this.address = address;
            return this;
        }

        public BankAccountBuilder withEmail(String email) {
            this.email = email;
            return this;
        }

        public BankAccountBuilder wantNewsletter(boolean newsletter) {
            this.newsletter = newsletter;
            return this;
        }
        public BankAccountBuilder wantMobileBanking(boolean mobileBanking) {
            this.mobileBanking = mobileBanking;
            return this;
        }

        public BankAccount build() {
            validateUserObject();

            BankAccount bankAccount = new BankAccount(
                    this.name, this.accountNumber,
                    this.address, this.email,
                    this.newsletter, this.mobileBanking);

            return bankAccount;
        }

        private void validateUserObject() {
            if (this.newsletter && email == null) {
                throw new IllegalArgumentException("Email can't be null when client want to receive the new letter");
            }
        }
    }
    @Override
    public String toString() {
        return "BankAccount [name=" + name + ", accountNumber=" + accountNumber + ", address=" + address +  ", email=" + email + ", newsLetter=" + newsLetter + "]";
    }

}
