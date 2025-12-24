#include <stdio.h>

int main() {
    int arr[] = {1, 2, 3, 4, 2, 2, 5, 6, 2, 7};
    int n = sizeof(arr) / sizeof(arr[0]);
    int targetNumber = 2; // S? c?n d?m
    int count = 0;

    for (int i = 0; i < n; i++) {
        if (arr[i] == targetNumber) {
            count++;
        }
    }

    printf("So %d xuat hien %d lan trong mang.\n", targetNumber, count);

    return 0;
}