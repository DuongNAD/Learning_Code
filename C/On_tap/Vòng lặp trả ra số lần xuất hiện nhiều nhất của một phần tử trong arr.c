#include <stdio.h>

int timPhanTuXuatHienNhieuNhat(int arr[], int n) {
    int maxDem = 0, phanTuNhieuNhat;
    for (int i = 0; i < n; i++) {
        int dem = 0;
        for (int j = 0; j < n; j++) {
            if (arr[i] == arr[j]) {
                dem++;
            }
        }
        if (dem > maxDem) {
            maxDem = dem;
            phanTuNhieuNhat = arr[i];
        }
    }
    return phanTuNhieuNhat;
}

int main() {
    int arr[] = {1, 2, 2, 3, 2, 4, 2, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Phan tu xuat hien nhieu nhat: %d\n", timPhanTuXuatHienNhieuNhat(arr, n));

    return 0;
}