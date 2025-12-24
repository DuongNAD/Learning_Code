#include <stdio.h>

int findSecondLargest(int arr[], int n) {
    int largest = arr[0], secondLargest = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > largest) {
            secondLargest = largest;
            largest = arr[i];
        } else if (arr[i] > secondLargest && arr[i] != largest) {
            secondLargest = arr[i];
        }
    }
    return secondLargest;
}

int main() {
    int arr[] = {1, 5, 2, 8, 3, 9, 4, 7, 6};
    int n = sizeof(arr) / sizeof(arr[0]);
    printf("So lon thu hai: %d\n", findSecondLargest(arr, n));
    return 0;
}