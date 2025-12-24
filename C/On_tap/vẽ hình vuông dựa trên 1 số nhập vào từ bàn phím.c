#include <stdio.h>

int main() {
    int n;

    printf("Nhap kich thuoc hinh vuong (n): ");
    scanf("%d", &n);

    printf("OUTPUT:\n");

    // In hàng đầu tiên của hình vuông
    for (int j = 1; j <= n; j++) {
        printf("%d ", j);
    }
    printf("\n");

    // In các hàng giữa của hình vuông
    for (int i = 0; i < n - 2; i++) {
        printf("1");
        for (int j = 0; j < (n - 2) * 2; j++) {
            printf(" "); // In khoảng trắng
        }
        printf("%d\n", n);
    }

    // In hàng cuối cùng của hình vuông
    for (int j = 1; j <= n; j++) {
        printf("%d ", j);
    }
    printf("\n");

    printf("Press any key to continue . . .\n");
    getchar(); // Đọc ký tự dòng mới còn lại từ lần nhập trước
    getchar(); // Đợi người dùng nhấn phím

    return 0;
}