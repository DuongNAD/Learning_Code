#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool isPrime(int n) {
    if (n <= 1) {
        return false;
    }

    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            return false;
        }
    }

    return true;
}

int main() {
    int num;
    printf("Nhập một số nguyên: ");
    scanf("%d", &num);

    if (isPrime(num)) {
        printf("%d là số nguyên tố.\n", num);
    } else {
        printf("%d không phải là số nguyên tố.\n", num);
    }

    return 0;
}