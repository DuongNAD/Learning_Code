#include <stdio.h>

int demSoLanXuatHien(int arr[], int n, int so) {
    int dem = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] == so) {
            dem++;
        }
    }
    return dem;
}

int main() {
    int arr[] = {5, 10, 15, 20, 5, 25};
    int n = sizeof(arr) / sizeof(arr[0]);
    int so = 5;

    printf("So lan xuat hien cua %d: %d\n", so, demSoLanXuatHien(arr, n, so));

    return 0;
}