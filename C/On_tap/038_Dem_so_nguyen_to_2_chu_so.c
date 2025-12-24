#include <stdio.h>

int isPrime(int n) {
    if (n <= 1) return 0;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int main() {
    int n, count = 0;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (arr[i] >= 10 && arr[i] <= 99 && isPrime(arr[i])) {
            count++;
        }
    }

    printf("So nguyen to co 2 chu so: %d", count);
    return 0;
}
