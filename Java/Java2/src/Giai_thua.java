public class Giai_thua {

    /**
     * Tính giai thừa của một số nguyên không âm bằng đệ quy.
     * @param n Số cần tính giai thừa
     * @return Giai thừa của n
     */
    public static long factorial(int n) {
        // TRƯỜNG HỢP CƠ SỞ (BASE CASE)
        // Đây là điều kiện dừng của đệ quy.
        // Giai thừa của 0 và 1 đều là 1.
        if (n <= 1) {
            return 1;
        }

        // TRƯỜNG HỢP ĐỆ QUY (RECURSIVE CASE)
        // Hàm tự gọi lại chính nó với một giá trị nhỏ hơn (n - 1).
        // Ví dụ: 5! = 5 * 4!
        //       4! = 4 * 3!
        //       ...
        return n * factorial(n - 1);
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // Tính và in ra giai thừa của 5
        System.out.println(factorial(5));
    }
}