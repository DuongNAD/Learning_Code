#include <stdio.h>

int main() {
    int n, count, found = 0;
    scanf("%d", &n);
    int a[n];

    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    for (int i = 0; i < n; i++) {
        count = 0;
        for (int j = 0; j < n; j++) {
            if (a[i] == a[j]) count++;
        }
        if (count > n / 2) {
            printf("Phan tu xuat hien > n/2: %d", a[i]);
            found = 1;
            break;
        }
    }

    if (!found) printf("Khong co phan tu nao xuat hien > n/2");
    return 0;
}
