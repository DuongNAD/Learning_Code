#include <stdio.h>

void xoaPhanTuTrungLap(int arr[], int *n) {
    for (int i = 0; i < *n - 1; i++) {
        for (int j = i + 1; j < *n; j++) {
            if (arr[i] == arr[j]) {
                xoaPhanTu(arr, n, j);
                j--; // Giảm j vì mảng đã bị dịch chuyển
            }
        }
    }
}

int main() {
    int arr[100] = {1, 2, 2, 3, 4, 4, 5};
    int n = 7;

    xoaPhanTuTrungLap(arr, &n);

    printf("Mang sau khi xoa trung lap: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}