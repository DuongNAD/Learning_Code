#include <stdio.h>

int isPerfectNumber(int n) {
    int sum = 0;
    for (int i = 1; i <= n / 2; i++) {
        if (n % i == 0) sum += i;
    }
    return sum == n && n != 0;
}

int main() {
    int n, count = 0;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (isPerfectNumber(arr[i])) count++;
    }

    printf("So luong so hoan hao: %d", count);
    return 0;
}
