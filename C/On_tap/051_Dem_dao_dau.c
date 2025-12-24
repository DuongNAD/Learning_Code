#include <stdio.h>

int main() {
    int n, count = 0;
    scanf("%d", &n);
    int a[n];

    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    for (int i = 1; i < n; i++) {
        if ((a[i - 1] >= 0 && a[i] < 0) || (a[i - 1] < 0 && a[i] >= 0)) {
            count++;
        }
    }

    printf("So lan dao dau: %d", count);
    return 0;
}
