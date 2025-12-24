#include <stdio.h>

int tongPhanSo(int n) {
    return n * (n + 1) / 2;
}

int main() {
    int n;

    printf("Nhap n: ");
    scanf("%d", &n);

    printf("Tong phan so den %d la: %d\n", n, tongPhanSo(n));

    return 0;
}