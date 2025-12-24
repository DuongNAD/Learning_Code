#include <stdio.h>

int binhPhuongCongSoLe(int arr[], int n) {
    int tong = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 != 0) {
            tong += arr[i] * arr[i];
        }
    }
    return tong;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Tong binh phuong cac so le: %d\n", binhPhuongCongSoLe(arr, n));

    return 0;
}