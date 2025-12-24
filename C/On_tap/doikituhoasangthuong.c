#include <stdio.h>
#include <string.h>
#include <ctype.h>

void toLowerCase(char *str) {
    for (int i = 0; str[i] != '\0'; i++) {
        str[i] = tolower(str[i]);
    }
}

int main() {
    char str[100];

    printf("Nhập chuỗi: ");
    fgets(str, sizeof(str), stdin);

    // Xóa ký tự newline nếu có
    if (str[strlen(str) - 1] == '\n') {
        str[strlen(str) - 1] = '\0';
    }

    toLowerCase(str);

    printf("Chuỗi sau khi chuyển đổi: %s\n", str);

    return 0;
}