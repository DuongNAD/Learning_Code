#include <stdio.h>
#include <stdlib.h> // Cần thiết cho qsort

// Hàm so sánh cho qsort (sắp xếp tăng dần)
int compareAscending(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int main() {
    int arr[] = {5, 2, 9, 1, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);

    // Sắp xếp mảng sử dụng qsort
    qsort(arr, n, sizeof(int), compareAscending);

    // In mảng sau khi sắp xếp
    printf("Mang sau khi sap xep tang dan: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}