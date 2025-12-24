#include <stdio.h>

int main() {
    int arr[100]; // Giả sử mảng không quá 100 phần tử
    int n;

    printf("Nhap so luong phan tu cua mang: ");
    scanf("%d", &n);

    printf("Nhap cac phan tu cua mang:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    int uniqueArr[100]; // Mảng chứa các phần tử duy nhất
    int uniqueCount = 0;

    for (int i = 0; i < n; i++) {
        int isDuplicate = 0;
        for (int j = 0; j < uniqueCount; j++) {
            if (arr[i] == uniqueArr[j]) {
                isDuplicate = 1;
                break;
            }
        }
        if (!isDuplicate) {
            uniqueArr[uniqueCount++] = arr[i];
        }
    }

    printf("Mang sau khi loai bo phan tu trung lap:\n");
    for (int i = 0; i < uniqueCount; i++) {
        printf("%d ", uniqueArr[i]);
    }
    printf("\n");

    return 0;
}