#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, found = 0, minAbs = 1e9, res;
    scanf("%d", &n);
    int a[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
        if (a[i] < 0 && abs(a[i]) < minAbs) {
            minAbs = abs(a[i]);
            res = a[i];
            found = 1;
        }
    }

    if (found)
        printf("So am co tri tuyet doi nho nhat: %d", res);
    else
        printf("Khong co so am nao");

    return 0;
}
