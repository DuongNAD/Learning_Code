#include <stdio.h>

void hoanDoi(int arr[], int viTri1, int viTri2) {
    int temp = arr[viTri1];
    arr[viTri1] = arr[viTri2];
    arr[viTri2] = temp;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int viTri1, viTri2;

    printf("Nhap vi tri 1: ");
    scanf("%d", &viTri1);
    printf("Nhap vi tri 2: ");
    scanf("%d", &viTri2);

    hoanDoi(arr, viTri1, viTri2);

    printf("Mang sau khi hoan doi: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}