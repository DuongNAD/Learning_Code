#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char str[100];

    printf("Nhap chuoi: ");
    fgets(str, sizeof(str), stdin);
    str[strcspn(str, "\n")] = 0; // Loại bỏ ký tự newline

    int len = strlen(str);

    if (len > 0) { // Kiểm tra chuỗi không rỗng
        str[len - 1] = toupper(str[len - 1]); // In hoa ký tự cuối cùng
    }

    printf("Chuoi sau khi xu ly: %s\n", str);

    return 0;
}