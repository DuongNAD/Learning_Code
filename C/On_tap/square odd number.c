#include <stdio.h>

void binhPhuongSoLe(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 != 0) {
            arr[i] *= arr[i];
        }
    }
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    binhPhuongSoLe(arr, n);

    printf("Day so sau khi binh phuong so le: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}