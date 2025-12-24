#include <stdio.h>
#include <stdlib.h> // Để sử dụng hàm abs()

int main() {
    int n;
    int count = 0;

    printf("Nhập số nguyên n: ");
    scanf("%d", &n);

    // Xử lý số âm
    n = abs(n);

    // Nếu n là 0, có 1 chữ số
    if (n == 0) {
        count = 1;
    } else {
        // Đếm số chữ số
        while (n != 0) {
            n /= 10;
            count++;
        }
    }

    printf("Số chữ số trong n là: %d\n", count);

    return 0;
}