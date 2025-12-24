#include <stdio.h>

int main() {
    int arr[100]; // Giả sử mảng không quá 100 phần tử
    int n;
    int sumOdd = 0, countOdd = 0;
    int sumEven = 0, countEven = 0;

    printf("Nhap so luong phan tu cua mang: ");
    scanf("%d", &n);

    printf("Nhap cac phan tu cua mang:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 == 0) {
            sumEven += arr[i];
            countEven++;
        } else {
            sumOdd += arr[i];
            countOdd++;
        }
    }

    if (countOdd > 0) {
        printf("Trung binh cong cac so le: %.2f\n", (float)sumOdd / countOdd);
    } else {
        printf("Khong co so le trong mang.\n");
    }

    if (countEven > 0) {
        printf("Trung binh cong cac so chan: %.2f\n", (float)sumEven / countEven);
    } else {
        printf("Khong co so chan trong mang.\n");
    }

    return 0;
}