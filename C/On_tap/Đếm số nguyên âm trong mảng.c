#include <stdio.h>

int demSoNguyenAm(int arr[], int n) {
    int dem = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] < 0) {
            dem++;
        }
    }
    return dem;
}

int main() {
    int arr[] = {-1, 2, -3, 4, -5};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("So luong so nguyen am trong mang: %d\n", demSoNguyenAm(arr, n));

    return 0;
}