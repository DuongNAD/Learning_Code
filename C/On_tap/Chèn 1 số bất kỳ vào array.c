#include <stdio.h>

void chenPhanTu(int arr[], int *n, int viTri, int giaTri) {
    if (viTri < 0 || viTri > *n) {
        printf("Vi tri khong hop le.\n");
        return;
    }
    (*n)++;
    for (int i = *n - 1; i > viTri; i--) {
        arr[i] = arr[i - 1];
    }
    arr[viTri] = giaTri;
}

int main() {
    int arr[] = {1, 2, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    int viTri, giaTri;

    printf("Nhap vi tri muon chen: ");
    scanf("%d", &viTri);
    printf("Nhap gia tri muon chen: ");
    scanf("%d", &giaTri);

    chenPhanTu(arr, &n, viTri, giaTri);

    printf("Mang sau khi chen: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}