#include <stdio.h>

int main() {
    int n, sum = 0;
    scanf("%d", &n); // Nhập số lượng phần tử
    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (arr[i] % 2 != 0) sum += arr[i]; // Nếu là số lẻ thì cộng vào tổng
    }

    printf("Tong cac phan tu le: %d", sum);
    return 0;
}
