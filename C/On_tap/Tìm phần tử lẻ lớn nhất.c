#include <stdio.h>

int main() {
    int n, arr[100], maxOdd = -1;
    printf("Nhap n: ");
    scanf("%d", &n);
    printf("Nhap mang: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (arr[i] % 2 != 0 && arr[i] > maxOdd) {
            maxOdd = arr[i];
        }
    }
    printf("Phan tu le lon nhat: %d\n", maxOdd);
    return 0;
}