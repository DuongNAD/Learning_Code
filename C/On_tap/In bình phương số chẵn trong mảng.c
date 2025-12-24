#include <stdio.h>

int main() {
    int arr[100], n, i;
    printf("Nhap so phan tu: ");
    scanf("%d", &n);
    printf("Nhap mang: ");
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    printf("Binh phuong cac so chan: ");
    for (i = 0; i < n; i++) {
        if (arr[i] % 2 == 0) {
            printf("%d ", arr[i] * arr[i]);
        }
    }
    return 0;
}