#include <stdio.h>

int daoNguocSo(int n) {
    int soDaoNguoc = 0;
    while (n > 0) {
        soDaoNguoc = soDaoNguoc * 10 + n % 10;
        n /= 10;
    }
    return soDaoNguoc;
}

int main() {
    int n;
    printf("Nhap so nguyen: ");
    scanf("%d", &n);

    printf("So dao nguoc: %d\n", daoNguocSo(n));

    return 0;
}