#include <stdio.h>

float tinhTrungBinhCongSoDuong(int arr[], int n) {
    int tong = 0, dem = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] > 0) {
            tong += arr[i];
            dem++;
        }
    }
    if (dem == 0) {
        return 0; // Không có số dương
    }
    return (float)tong / dem;
}

int main() {
    int arr[] = {1, -2, 3, -4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Trung binh cong so duong: %.2f\n", tinhTrungBinhCongSoDuong(arr, n));

    return 0;
}