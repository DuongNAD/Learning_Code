#include <stdio.h>

int timSoChanLonNhat(int arr[], int n) {
    int maxChan = -1;
    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 == 0 && arr[i] > maxChan) {
            maxChan = arr[i];
        }
    }
    return maxChan;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("So chan lon nhat: %d\n", timSoChanLonNhat(arr, n));

    return 0;
}