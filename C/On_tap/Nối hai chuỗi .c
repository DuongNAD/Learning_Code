#include <stdio.h>
#include <string.h>

int main() {
    char str1[100], str2[100];
    printf("Nhap chuoi 1: ");
    fgets(str1, sizeof(str1), stdin);
    printf("Nhap chuoi 2: ");
    fgets(str2, sizeof(str2), stdin);
    str1[strlen(str1) - 1] = '\0'; // Loại bỏ ký tự newline từ fgets
    strcat(str1, str2);
    printf("Chuoi sau khi noi: %s", str1);
    return 0;
}