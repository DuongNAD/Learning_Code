#include <stdio.h>

int isPrime(int n) {
    if (n < 2) return 0;
    for (int i = 2; i * i <= n; i++)
        if (n % i == 0) return 0;
    return 1;
}

int main() {
    int n;
    scanf("%d", &n);
    int a[n], printed[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
        printed[i] = 0;
    }

    printf("Cac so nguyen to khong trung:\n");
    for (int i = 0; i < n; i++) {
        if (!isPrime(a[i]) || printed[i]) continue;
        int isDuplicate = 0;
        for (int j = i + 1; j < n; j++) {
            if (a[i] == a[j]) {
                isDuplicate = 1;
                printed[j] = 1;
            }
        }
        if (!isDuplicate) {
            printf("%d ", a[i]);
        }
    }

    return 0;
}
