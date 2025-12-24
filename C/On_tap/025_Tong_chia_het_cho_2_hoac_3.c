#include <stdio.h>

int main() {
    int n, sum = 0;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (arr[i] % 2 == 0 || arr[i] % 3 == 0) {
            sum += arr[i];
        }
    }

    printf("Tong cac so chia het cho 2 hoac 3: %d", sum);
    return 0;
}
