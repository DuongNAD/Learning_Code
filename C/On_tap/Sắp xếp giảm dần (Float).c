#include <stdio.h>

void sapXepGiamDanFloat(float arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] < arr[j]) {
                float temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

int main() {
    float arr[] = {5.2, 2.8, 8.1, 1.9, 9.5};
    int n = sizeof(arr) / sizeof(arr[0]);

    sapXepGiamDanFloat(arr, n);

    printf("Mang sau khi sap xep giam dan (float): ");
    for (int i = 0; i < n; i++) {
        printf("%.2f ", arr[i]);
    }
    printf("\n");

    return 0;
}