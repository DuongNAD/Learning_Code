#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char str[100];

    printf("Nhap chuoi: ");
    fgets(str, sizeof(str), stdin);
    str[strcspn(str, "\n")] = 0;

    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i + 1] == ' ' || str[i + 1] == '\0') { // Nếu ký tự sau là khoảng trắng hoặc kết thúc chuỗi
            str[i] = toupper(str[i]); // In hoa ký tự hiện tại
        }
    }

    printf("Chuoi sau khi xu ly: %s\n", str);

    return 0;
}