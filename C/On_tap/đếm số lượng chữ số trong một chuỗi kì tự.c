#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char s[101]; // Mảng ký tự để lưu trữ chuỗi, tối đa 100 ký tự + ký tự kết thúc chuỗi '\0'
    int count = 0;

    printf("Nhap chuoi S (toi da 100 ky tu):\n");
    fgets(s, sizeof(s), stdin); // Đọc chuỗi từ người dùng, bao gồm cả dấu cách

    // Loại bỏ ký tự dòng mới ('\n') nếu có
    s[strcspn(s, "\n")] = 0;

    // Đếm số lượng chữ số trong chuỗi
    for (int i = 0; i < strlen(s); i++) {
        if (isdigit(s[i])) {
            count++;
        }
    }

    printf("OUTPUT:\n");
    printf("%d\n", count);

    printf("Press any key to continue . . .\n");
    getchar(); // Đọc ký tự dòng mới còn lại từ lần nhập trước
    getchar(); // Đợi người dùng nhấn phím

    return 0;
}