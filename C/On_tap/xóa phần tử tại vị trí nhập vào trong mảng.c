#include <stdio.h>

int main() {
    int n, index;

    // Nhập số lượng phần tử của mảng
    printf("Nhap so luong phan tu cua mang: ");
    scanf("%d", &n);

    int arr[n]; // Khai báo mảng với kích thước n

    // Nhập các phần tử của mảng
    printf("Nhap cac phan tu cua mang:\n");
    for (int i = 0; i < n; i++) {
        printf("arr[%d] = ", i);
        scanf("%d", &arr[i]);
    }

    // Nhập index cần xóa
    printf("Nhap index can xoa (0 - %d): ", n - 1);
    scanf("%d", &index);

    // Kiểm tra index hợp lệ
    if (index < 0 || index >= n) {
        printf("Index khong hop le.\n");
        return 1; // Kết thúc chương trình với mã lỗi
    }

    // Xóa phần tử tại index
    for (int i = index; i < n - 1; i++) {
        arr[i] = arr[i + 1];
    }

    // In mảng sau khi xóa
    printf("Mang sau khi xoa phan tu tai index %d:\n", index);
    for (int i = 0; i < n - 1; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}