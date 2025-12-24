#include <stdio.h>
#include <math.h>

int kiemTraNguyenTo(int n) {
    if (n <= 1) {
        return 0;
    }
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            return 0;
        }
    }
    return 1;
}

int timSoNguyenToDauTien(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        if (kiemTraNguyenTo(arr[i])) {
            return arr[i];
        }
    }
    return -1; // Không tìm thấy số nguyên tố
}

int main() {
    int arr[] = {4, 6, 8, 10, 11, 12};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("So nguyen to dau tien: %d\n", timSoNguyenToDauTien(arr, n));

    return 0;
}