#include <stdio.h>

int kiemTraMangTangDan(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        if (arr[i] < arr[i - 1]) {
            return 0; // Không tăng dần
        }
    }
    return 1; // Tăng dần
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Mang %s tang dan.\n", kiemTraMangTangDan(arr, n) ? "co" : "khong");

    return 0;
}