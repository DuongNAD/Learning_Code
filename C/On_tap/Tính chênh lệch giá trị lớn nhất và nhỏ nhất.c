#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, arr[100], min = 1000000, max = -1;
    printf("Nhap n: ");
    scanf("%d", &n);
    printf("Nhap mang: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (arr[i] < min) min = arr[i];
        if (arr[i] > max) max = arr[i];
    }
    printf("Chenh lech: %d\n", abs(max - min));
    return 0;
}