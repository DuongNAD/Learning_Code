#include <stdio.h>

void inSoChanViTriChanVaSort(int arr[], int n) {
    int chanViTriChan[n];
    int dem = 0;

    // Lọc số chẵn ở vị trí chẵn
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0 && arr[i] % 2 == 0) {
            chanViTriChan[dem++] = arr[i];
        }
    }

    // Sắp xếp tăng dần
    for (int i = 0; i < dem - 1; i++) {
        for (int j = i + 1; j < dem; j++) {
            if (chanViTriChan[i] > chanViTriChan[j]) {
                int temp = chanViTriChan[i];
                chanViTriChan[i] = chanViTriChan[j];
                chanViTriChan[j] = temp;
            }
        }
    }

    // In kết quả
    printf("Cac so chan tai vi tri chan sau khi sap xep: ");
    for (int i = 0; i < dem; i++) {
        printf("%d ", chanViTriChan[i]);
    }
    printf("\n");
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int n = sizeof(arr) / sizeof(arr[0]);

    inSoChanViTriChanVaSort(arr, n);

    return 0;
}