#include <stdio.h>

int giaiThua(int n) {
    if (n == 0) {
        return 1;
    }
    return n * giaiThua(n - 1);
}

int main() {
    int n;

    printf("Nhap n: ");
    scanf("%d", &n);

    printf("Giai thua cua %d la: %d\n", n, giaiThua(n));

    return 0;
}