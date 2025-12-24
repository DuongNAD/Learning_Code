#include <stdio.h>
#include <stdbool.h> // Thêm thư viện stdbool.h để sử dụng kiểu bool

// Hàm kiểm tra số nguyên tố
bool laSoNguyenTo(int num) {
    if (num <= 1) {
        return false;
    }
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int n, count = 0, num;

    do {
        printf("Nhập số n (0 <= n <= 100): ");
        scanf("%d", &n);
    } while (n < 0 || n > 100);

    num = n + 1; // Bắt đầu tìm số nguyên tố từ số lớn hơn n

    printf("4 số nguyên tố lớn hơn %d là:\n", n);

    while (count < 4) {
        if (laSoNguyenTo(num)) {
            printf("%d\n", num);
            count++;
        }
        num++;
    }

    return 0;
}