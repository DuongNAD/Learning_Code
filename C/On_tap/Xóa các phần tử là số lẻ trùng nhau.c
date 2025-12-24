#include <stdio.h>

int xoaSoLeTrungNhau(int arr[], int n) {
    if (n == 0 || n == 1) {
        return n;
    }

    int j = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 == 0) { // Nếu là số chẵn, giữ nguyên
            arr[j++] = arr[i];
        } else { // Nếu là số lẻ
            int trungNhau = 0;
            for (int k = 0; k < j; k++) {
                if (arr[k] == arr[i]) {
                    trungNhau = 1;
                    break;
                }
            }
            if (!trungNhau) {
                arr[j++] = arr[i];
            }
        }
    }
    return j;
}

int main() {
    int arr[] = {1, 2, 3, 4, 3, 5, 6, 5, 7, 8};
    int n = sizeof(arr) / sizeof(arr[0]);

    n = xoaSoLeTrungNhau(arr, n);

    printf("Mang sau khi xoa so le trung nhau: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}