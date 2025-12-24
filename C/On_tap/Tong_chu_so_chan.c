#include <stdio.h>

int sumDigits(int n) {
    int sum = 0;
    n = (n < 0) ? -n : n;
    while (n) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int main() {
    int n, total = 0;
    scanf("%d", &n);
    int a[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
        if (a[i] % 2 == 0) {
            total += sumDigits(a[i]);
        }
    }

    printf("Tong chu so cua cac phan tu chan: %d", total);
    return 0;
}
