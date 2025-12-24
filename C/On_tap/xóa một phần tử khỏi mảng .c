#include <stdio.h>

void xoaPhanTu(int arr[], int *n, int viTri) {
    if (viTri < 0 || viTri >= *n) {
        printf("Vi tri xoa khong hop le.\n");
        return;
    }

    for (int i = viTri; i < *n - 1; i++) {
        arr[i] = arr[i + 1];
    }

    (*n)--;
}

int main() {
    int arr[100] = {1, 2, 3, 4, 5};
    int n = 5;
    int viTriXoa = 2;

    xoaPhanTu(arr, &n, viTriXoa);

    printf("Mang sau khi xoa: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}