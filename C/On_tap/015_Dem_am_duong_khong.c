#include <stdio.h>

int main() {
    int n, am = 0, duong = 0, khong = 0;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (arr[i] > 0) duong++;
        else if (arr[i] < 0) am++;
        else khong++;
    }

    printf("So am: %d\nSo duong: %d\nSo 0: %d", am, duong, khong);
    return 0;
}
