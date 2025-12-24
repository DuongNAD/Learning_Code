#include <stdio.h>

int main() {
    int n, x, sum = 0, count = 0;
    scanf("%d %d", &n, &x);
    int a[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
        if (a[i] < x) {
            sum += a[i];
            count++;
        }
    }

    if (count)
        printf("TBC cac phan tu < %d: %.2f", x, (float)sum / count);
    else
        printf("Khong co phan tu nao < %d", x);

    return 0;
}
