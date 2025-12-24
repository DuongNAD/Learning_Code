

import java.util.*;
import java.util.Map.Entry; // Import thêm để dùng Entry

public class HashTableVsHashMapDemo {

    public static void main(String[] args) {
        System.out.println("=== HASHTABLE vs HASHMAP ===");

        demoHashtable();
        demoHashMap();
        demoContactList();
        demoAllowNull();
        demoSortHashMap();
    }

    // 1. Hashtable Demo
    // (Không cho phép key/value là null, và đã được đồng bộ hóa)
    static void demoHashtable() {
        System.out.println("\n--- 1. Demo Hashtable ---");
        Hashtable<String, String> table = new Hashtable<>();

        table.put("Alice", "123");
        table.put("Bob", "456");
        // table.put(null, "test"); // Sẽ ném ra NullPointerException
        // table.put("Charlie", null); // Sẽ ném ra NullPointerException

        System.out.println("Hashtable: " + table);
        System.out.println("Get Bob: " + table.get("Bob"));
    }

    // 2. HashMap Demo
    // (Cho phép 1 key null và nhiều value null, không đồng bộ)
    static void demoHashMap() {
        System.out.println("\n--- 2. Demo HashMap ---");
        HashMap<String, String> map = new HashMap<>();

        map.put("Alice", "123");
        map.put("Bob", "456");
        map.put("Alice", "999"); // Ghi đè giá trị của key "Alice"
        map.put(null, "Đây là key null"); // OK
        map.put("Charlie", null); // OK
        map.put("David", null); // OK

        System.out.println("HashMap: " + map);

        // Duyệt qua HashMap
        System.out.println("Duyệt HashMap:");
        for (Entry<String, String> entry : map.entrySet()) {
            System.out.println("Key: " + entry.getKey() + ", Value: " + entry.getValue());
        }
    }

    // 3. Ví dụ danh bạ
    static void demoContactList() {
        System.out.println("\n--- 3. Demo Danh bạ (dùng HashMap) ---");
        HashMap<String, String> contacts = new HashMap<>();
        contacts.put("An", "0909123456");
        contacts.put("Bình", "0912987654");
        contacts.put("Cường", "0988111222");

        // Lấy SĐT của Bình
        String binhPhone = contacts.get("Bình");
        System.out.println("SĐT của Bình: " + binhPhone);

        // Kiểm tra xem có SĐT của "Dũng" không
        if (contacts.containsKey("Dũng")) {
            System.out.println("SĐT của Dũng: " + contacts.get("Dũng"));
        } else {
            System.out.println("Không tìm thấy Dũng trong danh bạ.");
        }
    }

    // 4. Demo về việc cho phép null
    static void demoAllowNull() {
        System.out.println("\n--- 4. Demo Cho phép Null ---");

        // Thử với Hashtable (sẽ ném lỗi)
        try {
            Hashtable<String, String> table = new Hashtable<>();
            table.put(null, "Giá trị null");
        } catch (NullPointerException e) {
            System.out.println("Hashtable đã ném lỗi khi thêm key null: " + e.getMessage());
        }

        try {
            Hashtable<String, String> table = new Hashtable<>();
            table.put("Key", null);
        } catch (NullPointerException e) {
            System.out.println("Hashtable đã ném lỗi khi thêm value null: " + e.getMessage());
        }

        // Thử với HashMap (sẽ OK)
        HashMap<String, String> map = new HashMap<>();
        map.put(null, "Giá trị cho key null");
        map.put("Key cho value null", null);
        System.out.println("HashMap cho phép null: " + map);
    }

    // 5. Demo Sắp xếp HashMap
    // (Bản thân HashMap không có thứ tự, ta phải dùng cách khác để sắp xếp)
    static void demoSortHashMap() {
        System.out.println("\n--- 5. Demo Sắp xếp HashMap ---");
        HashMap<String, Integer> scores = new HashMap<>();
        scores.put("David", 85);
        scores.put("Alice", 92);
        scores.put("Charlie", 78);
        scores.put("Bob", 92);

        System.out.println("HashMap ban đầu (không theo thứ tự): " + scores);

        // Cách 1: Sắp xếp theo Key (dùng TreeMap)
        // TreeMap tự động sắp xếp các entry theo thứ tự tự nhiên của key
        TreeMap<String, Integer> sortedByKey = new TreeMap<>(scores);
        System.out.println("Sắp xếp theo Key (dùng TreeMap): " + sortedByKey);

        // Cách 2: Sắp xếp theo Value (phức tạp hơn)
        // 1. Chuyển entrySet sang List
        List<Entry<String, Integer>> list = new ArrayList<>(scores.entrySet());

        // 2. Sắp xếp List bằng Comparator
        Collections.sort(list, new Comparator<Entry<String, Integer>>() {
            public int compare(Entry<String, Integer> o1, Entry<String, Integer> o2) {
                // Sắp xếp theo giá trị (value) tăng dần
                // Để giảm dần, đổi o1.getValue() và o2.getValue()
                return o1.getValue().compareTo(o2.getValue());
            }
        });

        // 3. (Tùy chọn) Đổ lại vào LinkedHashMap để giữ thứ tự sau khi sắp xếp
        LinkedHashMap<String, Integer> sortedByValue = new LinkedHashMap<>();
        for (Entry<String, Integer> entry : list) {
            sortedByValue.put(entry.getKey(), entry.getValue());
        }

        System.out.println("Sắp xếp theo Value (tăng dần): " + sortedByValue);
    }
}