#include <stdio.h>
#include <string.h>

int main() {
    char str[100];
    int count = 0;

    printf("Nhập chuỗi: ");
    fgets(str, sizeof(str), stdin);

    // Xóa ký tự newline nếu có
    if (str[strlen(str) - 1] == '\n') {
        str[strlen(str) - 1] = '\0';
    }

    count = strlen(str);

    printf("Số lượng ký tự trong chuỗi là: %d\n", count);

    return 0;
}