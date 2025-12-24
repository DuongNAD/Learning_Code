#include <stdio.h>

int main() {
    int n;

    printf("Nhap so phan tu cua mang: ");
    scanf("%d", &n);

    int mang[n]; // Khai báo mảng với n phần tử

    // Nhập các phần tử của mảng
    printf("Nhap cac phan tu cua mang:\n");
    for (int i = 0; i < n; i++) {
        printf("Phan tu thu %d: ", i + 1);
        scanf("%d", &mang[i]);
    }

    // In ra các số lẻ trong mảng
    printf("Cac so le trong mang la: ");
    for (int i = 0; i < n; i++) {
        if (mang[i] % 2 != 0) {
            printf("%d ", mang[i]);
        }
    }
    printf("\n");

    printf("Press any key to continue . . .\n");
    getchar(); // Đọc ký tự dòng mới còn lại từ lần nhập trước
    getchar(); // Đợi người dùng nhấn phím

    return 0;
}