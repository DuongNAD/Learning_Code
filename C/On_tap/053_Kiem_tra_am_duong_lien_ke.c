#include <stdio.h>

int main() {
    int n, found = 0;
    scanf("%d", &n);
    int a[n];

    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    for (int i = 0; i < n - 1; i++) {
        if ((a[i] < 0 && a[i + 1] > 0) || (a[i] > 0 && a[i + 1] < 0)) {
            found = 1;
            break;
        }
    }

    if (found)
        printf("Mang co cap am duong lien ke");
    else
        printf("Mang khong co cap am duong lien ke");

    return 0;
}
