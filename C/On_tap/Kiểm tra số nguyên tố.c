#include <stdio.h>
#include <math.h>

int kiemTraNguyenTo(int n) {
    if (n <= 1) return 0;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int main() {
    int n;
    printf("Nhap so nguyen duong n: ");
    scanf("%d", &n);
    if (kiemTraNguyenTo(n)) {
        printf("%d la so nguyen to.\n", n);
    } else {
        printf("%d khong la so nguyen to.\n", n);
    }
    return 0;
}