#include <stdio.h>

int main() {
    int so1, so2, temp;

    printf("Nhập số thứ nhất: ");
    scanf("%d", &so1);

    printf("Nhập số thứ hai: ");
    scanf("%d", &so2);

    printf("Trước khi hoán đổi: số thứ nhất = %d, số thứ hai = %d\n", so1, so2);

    // Hoán đổi giá trị của hai số
    temp = so1;
    so1 = so2;
    so2 = temp;

    printf("Sau khi hoán đổi: số thứ nhất = %d, số thứ hai = %d\n", so1, so2);

    return 0;
}