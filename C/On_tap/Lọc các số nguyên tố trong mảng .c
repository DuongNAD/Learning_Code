#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool kiemTraNguyenTo(int n) {
    if (n <= 1) return false;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int locSoNguyenTo(int arr[], int n, int result[]) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (kiemTraNguyenTo(arr[i])) {
            result[count++] = arr[i];
        }
    }
    return count;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);
    int result[n];
    int size = locSoNguyenTo(arr, n, result);
    printf("Mang sau khi loc cac so nguyen to: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}