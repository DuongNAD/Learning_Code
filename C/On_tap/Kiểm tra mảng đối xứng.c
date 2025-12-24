#include <stdio.h>
#include <stdbool.h>

bool isSymmetric(int arr[], int n) {
    for (int i = 0; i < n / 2; i++) {
        if (arr[i] != arr[n - i - 1]) return false;
    }
    return true;
}

int main() {
    int arr1[] = {1, 2, 3, 2, 1};
    int arr2[] = {1, 2, 3, 4, 5};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);
    int n2 = sizeof(arr2) / sizeof(arr2[0]);
    printf("arr1 co doi xung: %s\n", isSymmetric(arr1, n1) ? "true" : "false");
    printf("arr2 co doi xung: %s\n", isSymmetric(arr2, n2) ? "true" : "false");
    return 0;
}