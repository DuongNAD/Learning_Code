package Java2_Day2;

public class KeyValuePairExample {
    public static void main(String[] args) {
        // Khởi tạo instance với giá trị cụ thể (Argument)
        // Ví dụ: key là "StudentName", value là 12345
        KeyValuePair<String, Integer> entry = new KeyValuePair<>("Nguyen Anh Duong", 12345);

        String name = entry.getKey();
        Integer id = entry.getValue();

        System.out.println("Name = " + name + ", Id = " + id);

        // Thử nghiệm với class ContactEntry
        ContactEntry contact = new ContactEntry("Hotline", 1900);
        System.out.println("Contact: " + contact.getKey() + " - " + contact.getValue());
    }
}