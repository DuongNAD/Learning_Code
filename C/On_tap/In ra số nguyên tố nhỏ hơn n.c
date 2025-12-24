#include <stdio.h>
#include <stdbool.h>
#include <math.h>

// Hàm kiểm tra số nguyên tố
bool laSoNguyenTo(int n) {
    if (n <= 1) return false;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    int n;
    printf("Nhap mot so nguyen duong: ");
    scanf("%d", &n);

    printf("Cac so nguyen to nho hon %d la:\n", n);
    for (int i = 2; i < n; i++) {
        if (laSoNguyenTo(i)) {
            printf("%d ", i);
        }
    }
    printf("\n");

    return 0;
}