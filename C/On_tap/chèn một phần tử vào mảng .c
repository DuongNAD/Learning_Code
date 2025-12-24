#include <stdio.h>

void chenPhanTu(int arr[], int *n, int viTri, int giaTri) {
    if (viTri < 0 || viTri > *n) {
        printf("Vi tri chen khong hop le.\n");
        return;
    }

    for (int i = *n; i > viTri; i--) {
        arr[i] = arr[i - 1];
    }

    arr[viTri] = giaTri;
    (*n)++;
}

int main() {
    int arr[100] = {1, 2, 3, 4, 5};
    int n = 5;
    int viTriChen = 2;
    int giaTriChen = 10;

    chenPhanTu(arr, &n, viTriChen, giaTriChen);

    printf("Mang sau khi chen: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}