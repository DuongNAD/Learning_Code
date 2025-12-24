#include <stdio.h>

int main() {
    int n, found = 0;
    scanf("%d", &n);
    int a[n], count;

    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    for (int i = 0; i < n; i++) {
        count = 0;
        for (int j = 0; j < n; j++) {
            if (a[i] == a[j]) count++;
        }
        if (count == 1) {
            printf("Phan tu xuat hien 1 lan: %d", a[i]);
            found = 1;
            break;
        }
    }

    if (!found) printf("Khong co phan tu xuat hien 1 lan");
    return 0;
}
