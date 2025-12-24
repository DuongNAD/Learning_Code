#include <stdio.h>

int timGiaTriLonThuHai(int arr[], int n) {
    int max1 = arr[0], max2 = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max1) {
            max2 = max1;
            max1 = arr[i];
        } else if (arr[i] > max2 && arr[i] != max1) {
            max2 = arr[i];
        }
    }
    return max2;
}

int main() {
    int arr[] = {5, 12, 8, 20, 15};
    int n = sizeof(arr) / sizeof(arr[0]);
    printf("Gia tri lon thu hai trong mang la: %d\n", timGiaTriLonThuHai(arr, n));
    return 0;
}