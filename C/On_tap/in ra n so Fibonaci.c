#include <stdio.h>

int main() {
    int n;

    // Nhập số lượng số Fibonacci cần in
    printf("Nhap so luong so Fibonacci muon in: ");
    scanf("%d", &n);

    // Kiểm tra nếu n không hợp lệ
    if (n <= 0) {
        printf("So luong phai lon hon 0.\n");
        return 1;
    }

    int a = 0, b = 1, next;

    printf("Day Fibonacci voi %d so dau tien:\n", n);

    for (int i = 0; i < n; i++) {
        printf("%d ", a);
        next = a + b;
        a = b;
        b = next;
    }

    return 0;
}
