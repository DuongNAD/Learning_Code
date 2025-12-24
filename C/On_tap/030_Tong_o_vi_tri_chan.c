#include <stdio.h>

int main() {
    int n, sum = 0;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (i % 2 == 0) sum += arr[i];
    }

    printf("Tong cac phan tu tai vi tri chan: %d", sum);
    return 0;
}
