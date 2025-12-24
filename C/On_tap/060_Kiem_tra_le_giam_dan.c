#include <stdio.h>

int main() {
    int n, isValid = 1;
    scanf("%d", &n);
    int a[n];

    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    for (int i = 0; i < n; i++) {
        if (a[i] % 2 == 0) {
            isValid = 0;
            break;
        }
        if (i > 0 && a[i] >= a[i - 1]) {
            isValid = 0;
            break;
        }
    }

    if (isValid)
        printf("Mang toan le va giam dan");
    else
        printf("Mang khong thoa man dieu kien");

    return 0;
}
