#include <stdio.h>

int tinhTongPhanTuChan(int arr[], int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 == 0) {
            sum += arr[i];
        }
    }
    return sum;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);
    printf("Tong cac phan tu chan trong mang la: %d\n", tinhTongPhanTuChan(arr, n));
    return 0;
}