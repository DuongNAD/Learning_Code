#include <stdio.h>

int main() {
    int n, found = 0;
    scanf("%d", &n);
    int a[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
        if (!found && a[i] > 0 && a[i] % 4 == 0) {
            printf("So duong dau tien chia het cho 4: %d", a[i]);
            found = 1;
        }
    }

    if (!found)
        printf("Khong co so duong chia het cho 4");

    return 0;
}
