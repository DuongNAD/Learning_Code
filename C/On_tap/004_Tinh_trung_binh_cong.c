#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int arr[n];
    int sum = 0;

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        sum += arr[i];
    }

    double average = (double)sum / n;
    printf("Trung binh cong: %.2f", average);
    return 0;
}
