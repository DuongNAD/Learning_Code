#include <stdio.h>

int main() {
    int a, b, sum = 0;
    printf("Nhap khoang [a, b]: ");
    scanf("%d %d", &a, &b);
    for (int i = a; i <= b; i++) {
        if (kiemTraNguyenTo(i)) {
            sum += i;
        }
    }
    printf("Tong cac so nguyen to trong khoang [%d, %d] la: %d\n", a, b, sum);
    return 0;
}