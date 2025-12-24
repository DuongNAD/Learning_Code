package Java2_Day2;

// Class này cụ thể hóa K là String và V là Integer
public class ContactEntry extends KeyValuePair<String, Integer> {

    public ContactEntry(String key, Integer value) {
        // Gọi constructor của lớp cha (Superclass)
        super(key, value);
    }
}