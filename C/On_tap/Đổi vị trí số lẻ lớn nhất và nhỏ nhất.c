#include <stdio.h>

void doiViTriLe(int arr[], int n) {
    int maxLe = -1, minLe = 1000000;
    int viTriMax = -1, viTriMin = -1;

    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 != 0) { // Ki?m tra s? l?
            if (arr[i] > maxLe) {
                maxLe = arr[i];
                viTriMax = i;
            }
            if (arr[i] < minLe) {
                minLe = arr[i];
                viTriMin = i;
            }
        }
    }

    if (viTriMax != -1 && viTriMin != -1) {
        int temp = arr[viTriMax];
        arr[viTriMax] = arr[viTriMin];
        arr[viTriMin] = temp;
    }
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int n = sizeof(arr) / sizeof(arr[0]);

    doiViTriLe(arr, n);

    printf("Mang sau khi doi vi tri: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}