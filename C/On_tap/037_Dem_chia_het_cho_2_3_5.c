#include <stdio.h>

int main() {
    int n, count = 0;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (arr[i] % 2 == 0 && arr[i] % 3 == 0 && arr[i] % 5 == 0) {
            count++;
        }
    }

    printf("So luong phan tu chia het cho 2, 3 va 5: %d", count);
    return 0;
}
