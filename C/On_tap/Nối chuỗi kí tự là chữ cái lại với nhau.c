#include <stdio.h>

int main() {
    char s[100]; // Khai báo chuỗi s với kích thước tối đa 100 ký tự
    int i;

    printf("Nhập chuỗi: ");
    gets(s); // Nhập chuỗi từ người dùng

    printf("Các ký tự chữ cái trong chuỗi là: ");
    for (i = 0; s[i] != '\0'; i++) {
        if ((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z')) {
            printf("%c", s[i]);
        }
    }

    printf("\nChuỗi đã nhập là: ");
    puts(s); // In chuỗi đã nhập ra màn hình

    return 0;
}