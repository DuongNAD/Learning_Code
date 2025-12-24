#include <stdio.h>

int tinhTichCacChuSo(int n) {
    int tich = 1;
    while (n > 0) {
        tich *= n % 10;
        n /= 10;
    }
    return tich;
}

int main() {
    int n;
    printf("Nhap so nguyen: ");
    scanf("%d", &n);

    printf("Tich cac chu so cua %d la: %d\n", n, tinhTichCacChuSo(n));

    return 0;
}