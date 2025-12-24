#include <stdio.h>
#include <stdlib.h>  // dùng để cấp phát bộ nhớ động

// Hàm hoán đổi hai số
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Hàm sắp xếp mảng theo thứ tự tăng dần
void sortAscending(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] > arr[j]) {
                swap(&arr[i], &arr[j]);
            }
        }
    }
}

int main() {
    int n;
    int *arr;

    // Nhập số phần tử
    printf("Nhap so luong phan tu: ");
    scanf("%d", &n);

    // Cấp phát bộ nhớ cho mảng
    arr = (int *)malloc(n * sizeof(int));
    if (arr == NULL) {
        printf("Khong du bo nho!\n");
        return 1;
    }

    // Nhập các phần tử của mảng
    for (int i = 0; i < n; i++) {
        printf("Nhap phan tu thu %d: ", i + 1);
        scanf("%d", &arr[i]);
    }

    // Sắp xếp mảng theo thứ tự tăng dần
    sortAscending(arr, n);

    // In mảng sau khi sắp xếp
    printf("\nMang sau khi sap xep tang dan:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    // Giải phóng bộ nhớ
    free(arr);

    return 0;
}


