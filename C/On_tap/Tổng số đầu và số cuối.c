#include <stdio.h>

int tongSoDauVaSoCuoi(int arr[], int n) {
    if (n < 2) {
        return -1; // Mảng không đủ phần tử
    }
    return arr[0] + arr[n - 1];
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Tong so dau va so cuoi: %d\n", tongSoDauVaSoCuoi(arr, n));

    return 0;
}