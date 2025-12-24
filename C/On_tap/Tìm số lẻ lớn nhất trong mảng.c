#include <stdio.h>

int findLargestOddNumber(int arr[], int n) {
    int largestOdd = -1; // Khởi tạo với giá trị nhỏ nhất có thể

    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 != 0) { // Kiểm tra số lẻ
            if (largestOdd == -1 || arr[i] > largestOdd) {
                largestOdd = arr[i]; // Cập nhật số lẻ lớn nhất
            }
        }
    }

    return largestOdd;
}

int main() {
    int n;

    printf("Nhập số lượng phần tử (n): ");
    scanf("%d", &n);

    if (n <= 0) {
        printf("Số lượng phần tử phải lớn hơn 0.\n");
        return 1;
    }

    int arr[n]; // Mảng có kích thước n

    printf("Nhập %d phần tử:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    int largestOdd = findLargestOddNumber(arr, n);

    if (largestOdd == -1) {
        printf("There are no odd numbers in %d elements.\n", n);
    } else {
        printf("%d\n", largestOdd);
    }

    return 0;
}