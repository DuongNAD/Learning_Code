#include <stdio.h>

int main() {
    int arr[7];
    int i, j, minIndex, temp;

    /* 1. Nhap 7 so nguyen vao mang */
    for (i = 0; i < 7; i++) {
        scanf("%d", &arr[i]);
    }

    /* 2. Thuc hien Selection Sort (Sap xep chon) */
    for (i = 0; i < 6; i++) {
        /* Tim phan tu nho nhat trong mang con lai */
        minIndex = i;
        for (j = i + 1; j < 7; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }

        /* Doi cho (swap) phan tu nho nhat voi phan tu dau tien (arr[i]) */
        temp = arr[i];
        arr[i] = arr[minIndex];
        arr[minIndex] = temp;
    }

    /* 3. In mang da sap xep */
    printf("OUTPUT:\n");
    for (i = 0; i < 7; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}