#include <stdio.h>

int main() {
    int arr[] = {1, 4, 7, 10, 13, 16, 19};
    int n = sizeof(arr) / sizeof(arr[0]);
    int maxPrime = -1;
    for (int i = 0; i < n; i++) {
        if (kiemTraNguyenTo(arr[i]) && arr[i] > maxPrime) {
            maxPrime = arr[i];
        }
    }
    if (maxPrime != -1) {
        printf("So nguyen to lon nhat trong mang la: %d\n", maxPrime);
    } else {
        printf("Khong co so nguyen to trong mang.\n");
    }
    return 0;
}