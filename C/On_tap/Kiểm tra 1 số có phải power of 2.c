#include <stdio.h>

int kiemTraPowerOf2(int n) {
    if (n <= 0) {
        return 0;
    }
    while (n % 2 == 0) {
        n /= 2;
    }
    return n == 1;
}

int main() {
    int n;
    printf("Nhap so nguyen: ");
    scanf("%d", &n);

    if (kiemTraPowerOf2(n)) {
        printf("%d la power of 2.\n", n);
    } else {
        printf("%d khong phai power of 2.\n", n);
    }

    return 0;
}