#include <stdio.h>

int main() {
    int n, isIncreasing = 1;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (i > 0 && arr[i] < arr[i - 1]) {
            isIncreasing = 0;
        }
    }

    if (isIncreasing)
        printf("Mang tang dan");
    else
        printf("Mang khong tang dan");

    return 0;
}
