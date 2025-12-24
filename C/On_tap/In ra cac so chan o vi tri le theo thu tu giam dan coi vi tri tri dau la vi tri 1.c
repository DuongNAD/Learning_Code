#include <stdio.h>

void inSoChanViTriLeGiamDan(int arr[], int n) {
    int chanViTriLe[n];
    int dem = 0;

    // Lọc số chẵn ở vị trí lẻ
    for (int i = 0; i < n; i++) {
        if (i % 2 != 0 && arr[i] % 2 == 0) {
            chanViTriLe[dem++] = arr[i];
        }
    }

    // Sắp xếp giảm dần
    for (int i = 0; i < dem - 1; i++) {
        for (int j = i + 1; j < dem; j++) {
            if (chanViTriLe[i] < chanViTriLe[j]) {
                int temp = chanViTriLe[i];
                chanViTriLe[i] = chanViTriLe[j];
                chanViTriLe[j] = temp;
            }
        }
    }

    // In kết quả
    printf("Cac so chan tai vi tri le theo thu tu giam dan: ");
    for (int i = 0; i < dem; i++) {
        printf("%d ", chanViTriLe[i]);
    }
    printf("\n");
}

int main() {
    int arr[] = {1, 2