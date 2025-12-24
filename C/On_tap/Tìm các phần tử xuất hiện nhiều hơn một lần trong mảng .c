#include <stdio.h>

void timPhanTuXuatHienNhieuHonMotLan(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        int count = 0;
        for (int j = 0; j < n; j++) {
            if (arr[i] == arr[j]) {
                count++;
            }
        }
        if (count > 1) {
            int found = 0;
            for (int k = 0; k < i; k++) {
                if (arr[i] == arr[k]) {
                    found = 1;
                    break;
                }
            }
            if (!found) {
                printf("%d ", arr[i]);
            }
        }
    }
    printf("\n");
}

int main() {
    int arr[] = {1, 2, 3, 2, 4, 1, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    timPhanTuXuatHienNhieuHonMotLan(arr, n);
    return 0;
}