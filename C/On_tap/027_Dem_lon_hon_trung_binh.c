#include <stdio.h>

int main() {
    int n, sum = 0, count = 0;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        sum += arr[i];
    }

    double avg = (double)sum / n;

    for (int i = 0; i < n; i++) {
        if (arr[i] > avg) count++;
    }

    printf("So luong phan tu lon hon trung binh: %d", count);
    return 0;
}
