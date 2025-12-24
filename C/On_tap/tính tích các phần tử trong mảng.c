#include <stdio.h>

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    long long product = 1;

    for (int i = 0; i < n; i++) {
        product *= arr[i];
    }

    printf("Tich cac phan tu trong mang: %lld\n", product);

    return 0;
}