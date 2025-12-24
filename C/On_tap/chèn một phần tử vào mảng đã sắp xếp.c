#include <stdio.h>

void chenPhanTuVaoMangDaSapXep(int arr[], int *n, int giaTri) {
    int viTriChen = *n;
    for (int i = 0; i < *n; i++) {
        if (arr[i] > giaTri) {
            viTriChen = i;
            break;
        }
    }

    chenPhanTu(arr, n, viTriChen, giaTri);
}

int main() {
    int arr[100] = {1, 3, 5, 7, 9};
    int n = 5;
    int giaTriChen = 6;

    chenPhanTuVaoMangDaSapXep(arr, &n, giaTriChen);

    printf("Mang sau khi chen: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}