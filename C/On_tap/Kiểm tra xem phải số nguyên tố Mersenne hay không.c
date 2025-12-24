#include <stdio.h>
#include <math.h>

int main() {
    int n, p = 0;
    printf("Nhap so nguyen duong n: ");
    scanf("%d", &n);
    if (n <= 1) {
        printf("%d khong phai la so nguyen to Mersenne.\n", n);
        return 0;
    }
    while (pow(2, p) - 1 < n) {
        p++;
    }
    if (pow(2, p) - 1 == n && kiemTraNguyenTo(p)) {
        printf("%d la so nguyen to Mersenne.\n", n);
    } else {
        printf("%d khong phai la so nguyen to Mersenne.\n", n);
    }
    return 0;
}