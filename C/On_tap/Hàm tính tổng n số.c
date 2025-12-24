#include <stdio.h>

int tinhTongNSo(int arr[], int n) {
    int tong = 0;
    for (int i = 0; i < n; i++) {
        tong += arr[i];
    }
    return tong;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Tong n so: %d\n", tinhTongNSo(arr, n));

    return 0;
}