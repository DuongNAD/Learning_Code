#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char str[100];

    printf("Nhap chuoi: ");
    fgets(str, sizeof(str), stdin);
    str[strcspn(str, "\n")] = 0; // Loại bỏ ký tự newline

    if (str[0] != '\0') { // Kiểm tra chuỗi không rỗng
        str[0] = toupper(str[0]); // In hoa ký tự đầu tiên
    }

    printf("Chuoi sau khi xu ly: %s\n", str);

    return 0;
}