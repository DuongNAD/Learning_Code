#include <stdio.h>

int isFibo(int a[], int n) {
    if (n < 3) return 0;
    for (int i = 2; i < n; i++) {
        if (a[i] != a[i - 1] + a[i - 2]) return 0;
    }
    return 1;
}

int main() {
    int n;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);

    if (isFibo(arr, n))
        printf("Mang la day Fibonacci");
    else
        printf("Mang khong la day Fibonacci");

    return 0;
}
