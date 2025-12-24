#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool isArmstrong(int n) {
    int originalN = n;
    int sum = 0;
    int digits = 0;

    // Tính số chữ số
    while (originalN != 0) {
        digits++;
        originalN /= 10;
    }

    originalN = n;
    while (originalN != 0) {
        int remainder = originalN % 10;
        sum += pow(remainder, digits);
        originalN /= 10;
    }

    return sum == n;
}

int main() {
    int num;
    printf("Nhập một số nguyên: ");
    scanf("%d", &num);

    if (isArmstrong(num)) {
        printf("%d là số Armstrong.\n", num);
    } else {
        printf("%d không phải là số Armstrong.\n", num);
    }

    return 0;
}