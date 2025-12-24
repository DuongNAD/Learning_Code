#include <stdio.h>

void swapLargestSmallestOdd(int arr[], int n) {
    if (n <= 0) {
        return; // Không làm gì nếu mảng rỗng
    }

    int largestOdd = -1;
    int smallestOdd = -1;
    int largestOddIndex = -1;
    int smallestOddIndex = -1;

    // Tìm số lẻ lớn nhất và nhỏ nhất cùng với chỉ số của chúng
    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 != 0) { // Nếu là số lẻ
            if (largestOdd == -1 || arr[i] > largestOdd) {
                largestOdd = arr[i];
                largestOddIndex = i;
            }
            if (smallestOdd == -1 || arr[i] < smallestOdd) {
                smallestOdd = arr[i];
                smallestOddIndex = i;
            }
        }
    }

    // Hoán đổi nếu tìm thấy cả số lẻ lớn nhất và nhỏ nhất
    if (largestOddIndex != -1 && smallestOddIndex != -1) {
        int temp = arr[largestOddIndex];
        arr[largestOddIndex] = arr[smallestOddIndex];
        arr[smallestOddIndex] = temp;
    }
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

    swapLargestSmallestOdd(arr, n);

    // In mảng sau khi hoán đổi
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}