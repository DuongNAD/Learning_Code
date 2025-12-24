package Java2.Day4;

public class Engineer extends Person {
    private String certificate;
    public Engineer(int id, String gpCoder, String name) {
        super(id, name);
        this.certificate = certificate;
    }

    @Override
    public String toString() {
        return "Engineer [certificate=" + certificate + ", " + super.toString() + "]";
    }
}
