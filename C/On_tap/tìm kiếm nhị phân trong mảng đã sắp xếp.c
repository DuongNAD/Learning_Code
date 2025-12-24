#include <stdio.h>

int binarySearch(int arr[], int left, int right, int key) {
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == key) {
            return mid;
        }
        if (arr[mid] < key) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1; // Không tìm thấy
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    int key = 4;
    int result = binarySearch(arr, 0, n - 1, key);

    if (result != -1) {
        printf("Phan tu %d duoc tim thay tai vi tri %d\n", key, result);
    } else {
        printf("Phan tu %d khong duoc tim thay trong mang\n", key);
    }

    return 0;
}