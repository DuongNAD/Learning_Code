#include <stdio.h>

// Hàm hoán đổi 2 số
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Hàm sắp xếp mảng tăng dần (sử dụng thuật toán sắp xếp nổi bọt - Bubble Sort)
void sortAscending(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(&arr[j], &arr[j + 1]);
            }
        }
    }
}

int main() {
    int n;

    // Nhập số lượng phần tử
    printf("Nhap so luong phan tu: ");
    scanf("%d", &n);

    int arr[n];

    // Nhập các phần tử của mảng
    printf("Nhap %d so nguyen:\n", n);
    for (int i = 0; i < n; i++) {
        printf("arr[%d] = ", i);
        scanf("%d", &arr[i]);
    }

    // Lọc các số chẵn vào một mảng khác
    int evenArr[n];
    int evenCount = 0;

    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 == 0) {
            evenArr[evenCount] = arr[i];
            evenCount++;
        }
    }

    // Sắp xếp mảng chẵn theo thứ tự tăng dần
    sortAscending(evenArr, evenCount);

    // In ra các số chẵn đã sắp xếp
    printf("Cac so chan theo thu tu tang dan la:\n");
    for (int i = 0; i < evenCount; i++) {
        printf("%d ", evenArr[i]);
    }

    return 0;
}
