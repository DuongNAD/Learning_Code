#include <stdio.h>

int kiemTraMangDoiXung(int arr[], int n) {
    for (int i = 0; i < n / 2; i++) {
        if (arr[i] != arr[n - i - 1]) {
            return 0; // Không đối xứng
        }
    }
    return 1; // Đối xứng
}

int main() {
    int arr[] = {1, 2, 3, 2, 1};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Mang %s doi xung.\n", kiemTraMangDoiXung(arr, n) ? "co" : "khong");

    return 0;
}