#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char str[1000];
    char startChar, endChar;
    int count = 0;
    char *token;

    printf("Nhap chuoi: ");
    fgets(str, sizeof(str), stdin);
    // Loại bỏ ký tự newline nếu có
    if (str[strlen(str) - 1] == '\n') {
        str[strlen(str) - 1] = '\0';
    }

    printf("Nhap ky tu bat dau: ");
    scanf(" %c", &startChar);
    printf("Nhap ky tu ket thuc: ");
    scanf(" %c", &endChar);

    // Tách chuỗi thành các từ
    token = strtok(str, " ,.-"); // Sử dụng dấu cách, dấu phẩy, dấu chấm, dấu gạch ngang làm dấu phân cách
    while (token != NULL) {
        int len = strlen(token);
        if (len > 0 && tolower(token[0]) == tolower(startChar) && tolower(token[len - 1]) == tolower(endChar)) {
            count++;
        }
        token = strtok(NULL, " ,.-");
    }

    printf("So luong tu bat dau bang '%c' va ket thuc bang '%c': %d\n", startChar, endChar, count);

    return 0;
}