#include <stdio.h>

void timViTriTongBang(int arr[], int n, int tong) {
    for (int i = 0; i < n - 1; i++) {
        if (arr[i] + arr[i + 1] == tong) {
            printf("Vi tri: %d va %d\n", i, i + 1);
        }
    }
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    int tong;

    printf("Nhap tong can tim: ");
    scanf("%d", &tong);

    timViTriTongBang(arr, n, tong);

    return 0;
}