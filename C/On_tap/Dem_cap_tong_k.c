#include <stdio.h>

int main() {
    int n, k, count = 0;
    scanf("%d %d", &n, &k);
    int a[n];

    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (a[i] + a[j] == k) count++;
        }
    }

    printf("So cap co tong = %d: %d", k, count);
    return 0;
}
