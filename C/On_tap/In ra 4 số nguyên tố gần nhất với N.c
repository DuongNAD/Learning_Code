#include <stdio.h>
#include <math.h>

// Hàm kiểm tra số nguyên tố
int isPrime(int n) {
    if (n <= 1) return 0;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int main() {
    int n, count = 0, i = 1;
    printf("Nhap n: ");
    scanf("%d", &n);

    printf("4 so nguyen to gan n nhat la:\n");
    while (count < 4) {
        if (isPrime(n - i)) {
            printf("%d ", n - i);
            count++;
        }
        if (isPrime(n + i)) {
            printf("%d ", n + i);
            count++;
        }
        i++;
    }
    return 0;
}