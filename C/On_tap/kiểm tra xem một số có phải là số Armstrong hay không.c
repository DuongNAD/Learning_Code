#include <stdio.h>
#include <math.h>

int main() {
    int number, originalNumber, remainder, n = 0;
    float result = 0.

    printf("Nhap mot so nguyen: ");
    scanf("%d", &number);

    originalNumber = number;

    // Tính số chữ số
    while (originalNumber != 0) {
        originalNumber /= 10;
        ++n;
    }

    originalNumber = number;

    // Tính tổng lũy thừa của các chữ số
    while (originalNumber != 0) {
        remainder = originalNumber % 10;
        result += pow(remainder, n);
        originalNumber /= 10;
    }

    // Kiểm tra số Armstrong
    if ((int)result == number) {
        printf("%d la so Armstrong.\n", number);
    } else {
        printf("%d khong phai la so Armstrong.\n", number);
    }

    return 0;
}