#include <stdio.h>

void selectionSortDescending(int arr[], int n) {
    int i, j, maxIndex, temp;

    for (i = 0; i < n - 1; i++) {
        maxIndex = i;
        for (j = i + 1; j < n; j++) {
            if (arr[j] > arr[maxIndex]) {
                maxIndex = j;
            }
        }

        // Hoán đổi phần tử lớn nhất với phần tử đầu tiên của phần chưa được sắp xếp
        temp = arr[i];
        arr[i] = arr[maxIndex];
        arr[maxIndex] = temp;
    }
}

int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);

    selectionSortDescending(arr, n);

    printf("Mảng sau khi sắp xếp giảm dần: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}