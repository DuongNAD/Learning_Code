#include <stdio.h>
#include <stdlib.h> // Để sử dụng hàm abs()

int findAbsoluteDifference(int arr[], int n) {
    if (n <= 0) {
        return 0; // Trả về 0 nếu mảng rỗng hoặc có kích thước không hợp lệ
    }

    int max = arr[0];
    int min = arr[0];

    // Tìm giá trị lớn nhất và nhỏ nhất
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
        if (arr[i] < min) {
            min = arr[i];
        }
    }

    // Trả về giá trị tuyệt đối của hiệu
    return abs(max - min);
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

    int difference = findAbsoluteDifference(arr, n);

    printf("%d\n", difference);

    return 0;
}