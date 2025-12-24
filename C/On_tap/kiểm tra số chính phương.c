#include <stdio.h>
#include <math.h>
#include <stdbool.h>

bool laSoChinhPhuong(int n) {
    if (n < 0) {
        return false;
    }
    int sqrtN = sqrt(n);
    return sqrtN * sqrtN == n;
}

int main() {
    int n;

    printf("Nhap so nguyen n: ");
    scanf("%d", &n);

    if (laSoChinhPhuong(n)) {
        printf("%d la so chinh phuong.\n", n);
    } else {
        printf("%d khong la so chinh phuong.\n", n);
    }

    return 0;
}