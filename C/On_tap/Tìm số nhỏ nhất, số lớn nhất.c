#include <stdio.h>

void timMinMax(int arr[], int n, int *min, int *max) {
    *min = arr[0];
    *max = arr[0];

    for (int i = 1; i < n; i++) {
        if (arr[i] < *min) {
            *min = arr[i];
        }
        if (arr[i] > *max) {
            *max = arr[i];
        }
    }
}

int main() {
    int arr[] = {5, 2, 8, 1, 9};
    int n = sizeof(arr) / sizeof(arr[0]);
    int min, max;

    timMinMax(arr, n, &min, &max);

    printf("So nho nhat: %d\n", min);
    printf("So lon nhat: %d\n", max);

    return 0;
}