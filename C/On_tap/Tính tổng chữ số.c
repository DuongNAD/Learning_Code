#include <stdio.h>

int sumDigits(int n) {
    int sum = 0;
    while (n != 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int main() {
    int num;
    printf("Nhap mot so: ");
    scanf("%d", &num);
    printf("Tong cac chu so: %d\n", sumDigits(num));
    return 0;
}