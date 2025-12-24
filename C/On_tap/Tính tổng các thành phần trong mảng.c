#include <stdio.h>

int tinhTongMang(int arr[], int n) {
    int tong = 0;
    for (int i = 0; i < n; i++) {
        tong += arr[i];
    }
    return tong;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Tong cac phan tu trong mang: %d\n", tinhTongMang(arr, n));

    return 0;
}