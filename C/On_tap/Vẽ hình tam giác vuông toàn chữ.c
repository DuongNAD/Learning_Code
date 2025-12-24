#include <stdio.h>

int main() {
    int rows;
    char alphabet = 'A'; // Bắt đầu từ chữ 'A'

    printf("Nhập số hàng: ");
    scanf("%d", &rows);

    // Kiểm tra số hàng hợp lệ
    if (rows <= 0) {
        printf("Số hàng phải lớn hơn 0.\n");
        return 1; // Thoát chương trình với mã lỗi
    }

    // In hình tam giác nửa bảng chữ cái
    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%c", alphabet);
            alphabet++; // Tăng chữ cái tiếp theo
        }
        printf("\n"); // Xuống dòng sau mỗi hàng
    }

    return 0;
}