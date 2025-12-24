#include <stdio.h>

int main() {
    int n, sum = 0;
    scanf("%d", &n);
    int a[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
        if (i % 2 != 0 && a[i] % 3 == 0) {
            sum += a[i];
        }
    }

    printf("Tong cac phan tu o vi tri le chia het cho 3: %d", sum);
    return 0;
}
