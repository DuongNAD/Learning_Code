#include <stdio.h>

void sortEvenOdd(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if ((arr[i] % 2 == 0 && arr[j] % 2 == 0 && arr[i] > arr[j]) ||
                (arr[i] % 2 != 0 && arr[j] % 2 != 0 && arr[i] < arr[j])) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

int main() {
    int arr[] = {5, 2, 8, 1, 9, 4, 6, 3, 7};
    int n = sizeof(arr) / sizeof(arr[0]);
    sortEvenOdd(arr, n);
    printf("Mang sau khi sap xep: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    return 0;
}