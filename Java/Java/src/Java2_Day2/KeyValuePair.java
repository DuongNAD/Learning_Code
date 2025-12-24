package Java2_Day2;

// Sử dụng Generics K và V để định nghĩa kiểu dữ liệu linh hoạt
public class KeyValuePair<K, V> {
    private K key;
    private V value;

    // Constructor: Sử dụng K và V thay vì String/Integer cụ thể
    public KeyValuePair(K key, V value) {
        this.key = key;     // Gán tham số 'key' vào thuộc tính 'this.key'
        this.value = value; // Gán tham số 'value' vào thuộc tính 'this.value'
    }

    public K getKey() {
        return this.key;
    }

    public V getValue() {
        return this.value;
    }

    public void setKey(K key) {
        this.key = key;
    }

    public void setValue(V value) {
        this.value = value;
    }
}