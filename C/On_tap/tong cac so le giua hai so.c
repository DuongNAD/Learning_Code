#include <stdio.h>

int main() {
    int x, y, sum = 0;

    // Nhập x và y, đảm bảo x < y
    printf("Nhap x: ");
    scanf("%d", &x);

    printf("Nhap y (y > x): ");
    scanf("%d", &y);

    if (x >= y) {
        printf("Gia tri khong hop le! x phai nho hon y.\n");
        return 1; // Kết thúc chương trình nếu nhập sai
    }

    // Tính tổng các số lẻ từ x đến y
    for (int i = x; i <= y; i++) {
        if (i % 2 != 0) {
            sum += i;
        }
    }

    // In kết quả
    printf("Tong cac so le tu %d den %d la: %d\n", x, y, sum);

    return 0;
}
