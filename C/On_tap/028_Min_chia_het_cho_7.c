#include <stdio.h>
#include <limits.h>

int main() {
    int n, min7 = INT_MAX, found = 0;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (arr[i] % 7 == 0 && arr[i] < min7) {
            min7 = arr[i];
            found = 1;
        }
    }

    if (found)
        printf("So nho nhat chia het cho 7: %d", min7);
    else
        printf("Khong co so chia het cho 7");

    return 0;
}
