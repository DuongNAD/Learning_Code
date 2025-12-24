#include <stdio.h>

int findLargestOddNumber(int arr[], int n) {
    int largestOdd = -1; // Khởi tạo số lẻ lớn nhất là -1 (không có số lẻ)

    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 != 0) { // Kiểm tra nếu là số lẻ
            if (largestOdd == -1 || arr[i] > largestOdd) {
                largestOdd = arr[i]; // Cập nhật số lẻ lớn nhất
            }
        }
    }

    return largestOdd;
}

int main() {
    int n;

    // Nhập số lượng phần tử
    printf("INPUT:\n");
    scanf("%d", &n);

    // Nhập mảng
    int arr[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    // Tìm số lẻ lớn nhất
    int largestOdd = findLargestOddNumber(arr, n);

    // In kết quả
    printf("OUTPUT:\n");
    if (largestOdd != -1) {
        printf("%d\n", largestOdd);
    } else {
        printf("There are no odd numbers in %d elements.\n", n);
    }

    return 0;
}