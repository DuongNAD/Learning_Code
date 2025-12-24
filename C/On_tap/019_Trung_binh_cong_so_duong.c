#include <stdio.h>

int main() {
    int n, sum = 0, count = 0;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (arr[i] > 0) {
            sum += arr[i];
            count++;
        }
    }

    if (count == 0)
        printf("Khong co so duong");
    else
        printf("Trung binh cong cac so duong: %.2f", (float)sum / count);

    return 0;
}
