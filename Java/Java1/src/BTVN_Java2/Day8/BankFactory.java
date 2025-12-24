package BTVN_Java2.Day8;

public class BankFactory {
    private BankFactory() {}
    public static final Bank getBank(BankType bankType){
        switch (bankType){
            case TPBANK:
                return new TPBank();
            case VIETCOMBANK:
                return new VietcomBank();
                default:
                    throw new IllegalArgumentException("Bank type not found");
        }
    }
}
