# 🔄 Bảng Tra Cứu Cú Pháp: Java / C sang Python Cho Lập Trình Viên

> **Dành cho người đã vững tư duy C / Java**: Bản chất tư duy logic của bạn đã đúng 100%, bạn chỉ cần map cú pháp quen thuộc sang cách viết của Python.

---

## 1. Khởi Tạo Cấu Trúc Dữ Liệu

| Thao tác | Java | C / C++ | Python |
| :--- | :--- | :--- | :--- |
| **Mảng động (List)** | `List<Integer> a = new ArrayList<>();` | `std::vector<int> a;` | `a = []` |
| **Thêm phần tử** | `a.add(10);` | `a.push_back(10);` | `a.append(10)` |
| **Lấy kích thước** | `a.size();` | `a.size();` | `len(a)` |
| **Bảng băm (Map/Dict)**| `Map<String, Integer> m = new HashMap<>();` | `std::map<string, int> m;` | `m = {}` |
| **Thêm vào Map** | `m.put("apple", 5);` | `m["apple"] = 5;` | `m["apple"] = 5` |
| **Kiểm tra tồn tại** | `m.containsKey("apple")` | `m.find("apple") != m.end()` | `"apple" in m` |
| **Tập hợp (Set)** | `Set<Integer> s = new HashSet<>();` | `std::set<int> s;` | `s = set()` |

---

## 2. Vòng Lặp (Loops)

### Duyệt qua từng phần tử (For-Each)
- **Java**:
  ```java
  for (int x : numbers) {
      System.out.println(x);
  }
  ```
- **Python**:
  ```python
  for x in numbers:
      print(x)
  ```

### Duyệt theo chỉ số index (i = 0 đến n-1)
- **Java**:
  ```java
  for (int i = 0; i < numbers.size(); i++) {
      int x = numbers.get(i);
  }
  ```
- **Python**:
  ```python
  for i in range(len(numbers)):
      x = numbers[i]
  ```

### Duyệt lấy CẢ index VÀ giá trị (Siêu tiện trong Python)
- **Python**:
  ```python
  for i, x in enumerate(numbers):
      print(f"Chỉ số {i} có giá trị {x}")
  ```

---

## 3. Khai Báo Hàm & Giải Mã "Type Hints"

Trong Java, bạn bắt buộc phải khai báo kiểu nghiêm ngặt:
```java
public List<String> getWords(String text, int minLength) {
    ...
}
```

Trong Python:
- **Cách viết tự nhiên (Dynamic Typing - Khuyên dùng khi mới học)**:
  ```python
  def get_words(text, min_length):
      ...
  ```
  *Python không bắt buộc khai báo kiểu! Bạn truyền tham số thoải mái.*

- **Cách viết Type Hints (Thứ bạn thấy trong file bài tập gây ngợp)**:
  ```python
  from typing import List, Tuple, Dict
  def get_words(text: str, min_length: int) -> List[Tuple[str, int]]:
  ```
  - `text: str`: chú thích `text` là String (chỉ để gợi ý code, không ép buộc).
  - `-> List[Tuple[str, int]]`: tương đương `List<Pair<String, Integer>>` trong Java.
  - **Lưu ý**: Đây chỉ là **chú thích cho IDE**, khi chạy thực tế Python hoàn toàn bỏ qua chúng!

---

## 4. Xử Lý Chuỗi (String)

| Thao tác | Java | Python |
| :--- | :--- | :--- |
| **Cắt thành mảng từ** | `text.split(" ")` | `text.split()` *(tự bỏ qua khoảng trắng thừa)* |
| **Chữ thường** | `text.toLowerCase()` | `text.lower()` |
| **Cắt chuỗi con** | `text.substring(0, 3)` | `text[0:3]` *(cú pháp slice)* |
| **Lấy ký tự cuối** | `text.charAt(text.length() - 1)` | `text[-1]` *(chỉ số âm đếm ngược)* |
| **Nối mảng thành chuỗi**| `String.join(", ", list)` | `", ".join(list)` |

---

## 5. Đếm Tần Suất (Frequency Map)

- **Java**:
  ```java
  Map<String, Integer> counts = new HashMap<>();
  for (String word : words) {
      counts.put(word, counts.getOrDefault(word, 0) + 1);
  }
  ```
- **Python (Cách 1 - Tương đương Java)**:
  ```python
  counts = {}
  for word in words:
      counts[word] = counts.get(word, 0) + 1
  ```
- **Python (Cách 2 - Siêu ngắn bằng Counter)**:
  ```python
  from collections import Counter
  counts = Counter(words)  # Xong 1 dòng duy nhất!
  ```
