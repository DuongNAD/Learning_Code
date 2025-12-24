#include <stdio.h>

void selectionSortOdd(int arr[], int n) {
    int i, j, minIndex, temp;
    for (i = 0; i < n - 1; i++) {
        minIndex = i;
        for (j = i + 1; j < n; j++) {
            if (arr[j] % 2 != 0 && arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        if (arr[minIndex] % 2 != 0) {
            temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }
}

int main() {
    int arr[100], n, i;
    printf("Nhap so phan tu: ");
    scanf("%d", &n);
    printf("Nhap mang: ");
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    selectionSortOdd(arr, n);
    printf("Mang phan tu le tang dan: ");
    for (i = 0; i < n; i++) {
        if (arr[i] % 2 != 0) {
            printf("%d ", arr[i]);
        }
    }
    return 0;
}