#include <stdio.h>

int main() {
    int arr[] = {5, 2, 9, 1, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);
    double sum = 0;

    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }

    double average = sum / n;

    printf("Trung binh cong: %.2lf\n", average);

    return 0;
}