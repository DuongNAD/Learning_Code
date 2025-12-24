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

bool isMersenne(int n) {
    int p = 2;
    while (pow(2, p) - 1 <= n) {
        if (pow(2, p) - 1 == n && isPrime(p)) {
            return true;
        }
        p++;
    }
    return false;
}

int main() {
    int num;
    printf("Nhập một số nguyên: ");
    scanf("%d", &num);

    if (isMersenne(num)) {
        printf("%d là số Mersenne.\n", num);
    } else {
        printf("%d không phải là số Mersenne.\n", num);
    }

    return 0;
}