#include <stdio.h>
#include <limits.h>

int main() {
    int n, max = INT_MIN, found = 0;
    scanf("%d", &n);
    int a[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
        if (a[i] % 3 == 0 && a[i] % 7 == 0 && a[i] > max) {
            max = a[i];
            found = 1;
        }
    }

    if (found)
        printf("So lon nhat chia het cho 3 va 7: %d", max);
    else
        printf("Khong co so chia het cho 3 va 7");

    return 0;
}
