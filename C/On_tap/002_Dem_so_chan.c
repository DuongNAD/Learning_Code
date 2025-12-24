#include <stdio.h>

int main() {
    int n, count = 0;
    scanf("%d", &n); // Nhập số lượng phần tử
    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (arr[i] % 2 == 0) count++; // Nếu là số chẵn thì tăng biến đếm
    }

    printf("So luong so chan: %d", count);
    return 0;
}
