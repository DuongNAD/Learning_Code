#include <stdio.h>

int main() {
    int n, minIdx = 0, maxIdx = 0, sum = 0;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (arr[i] < arr[minIdx]) minIdx = i;
        if (arr[i] > arr[maxIdx]) maxIdx = i;
    }

    int start = (minIdx < maxIdx) ? minIdx + 1 : maxIdx + 1;
    int end = (minIdx > maxIdx) ? minIdx : maxIdx;

    for (int i = start; i < end; i++) {
        sum += arr[i];
    }

    printf("Tong giua min va max: %d", sum);
    return 0;
}
