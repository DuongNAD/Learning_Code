#include <stdio.h>

void timMinMaxThuHai(int arr[], int n, int *minThuHai, int *maxThuHai) {
    int min = arr[0], max = arr[0];
    *minThuHai = 1000000; // Giá trị lớn ban đầu
    *maxThuHai = -1000000; // Giá trị nhỏ ban đầu

    for (int i = 1; i < n; i++) {
        if (arr[i] < min) {
            *minThuHai = min;
            min = arr[i];
        } else if (arr[i] < *minThuHai && arr[i] != min) {
            *minThuHai = arr[i];
        }

        if (arr[i] > max) {
            *maxThuHai = max;
            max = arr[i];
        } else if (arr[i] > *maxThuHai && arr[i] != max) {
            *maxThuHai = arr[i];
        }
    }
}

int main() {
    int arr[] = {5, 2, 8, 1, 9, 7};
    int n = sizeof(arr) / sizeof(arr[0]);
    int minThuHai, maxThuHai;

    timMinMaxThuHai(arr, n, &minThuHai, &maxThuHai);

    printf("So nho thu hai: %d\n", minThuHai);
    printf("So lon thu hai: %d\n", maxThuHai);

    return 0;
}