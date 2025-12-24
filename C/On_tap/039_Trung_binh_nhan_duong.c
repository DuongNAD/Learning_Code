#include <stdio.h>
#include <math.h>

int main() {
    int n, count = 0;
    double product = 1;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (arr[i] > 0) {
            product *= arr[i];
            count++;
        }
    }

    if (count > 0)
        printf("Trung binh nhan cac so duong: %.2f", pow(product, 1.0 / count));
    else
        printf("Khong co so duong nao");

    return 0;
}
