#include <stdio.h>

int main() {
    int n, x;
    printf("Nhap n: ");
    scanf("%d", &n);
    int a[n];

    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    printf("Nhap gia tri x can tim: ");
    scanf("%d", &x);

    int found = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] == x) {
            printf("Tim thay x tai vi tri %d\n", i);
            found = 1;
        }
    }
    if (!found) printf("Khong tim thay x\n");
    return 0;
}