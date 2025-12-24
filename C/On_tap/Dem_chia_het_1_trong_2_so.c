#include <stdio.h>

int main() {
    int n, a, b, count = 0;
    scanf("%d %d %d", &n, &a, &b);
    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if ((arr[i] % a == 0) ^ (arr[i] % b == 0)) count++;
    }

    printf("So phan tu chi chia het cho 1 trong 2: %d", count);
    return 0;
}
