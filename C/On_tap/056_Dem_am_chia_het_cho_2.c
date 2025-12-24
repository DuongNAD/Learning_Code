#include <stdio.h>

int main() {
    int n, count = 0;
    scanf("%d", &n);
    int a[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
        if (a[i] < 0 && a[i] % 2 == 0) count++;
    }

    printf("So am chia het cho 2: %d", count);
    return 0;
}
