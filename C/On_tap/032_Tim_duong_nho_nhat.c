#include <stdio.h>
#include <limits.h>

int main() {
    int n, min = INT_MAX, found = 0;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (arr[i] > 0 && arr[i] < min) {
            min = arr[i];
            found = 1;
        }
    }

    if (found)
        printf("So duong nho nhat: %d", min);
    else
        printf("Khong co so duong nao");

    return 0;
}
