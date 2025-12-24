#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char str[100];

    printf("Nhap chuoi: ");
    fgets(str, sizeof(str), stdin);

    // Loại bỏ ký tự newline từ fgets
    str[strcspn(str, "\n")] = 0;

    for (int i = 0; str[i] != '\0'; i++) {
        if (i % 2 == 0) { // Vị trí lẻ (bắt đầu từ 0)
            str[i] = toupper(str[i]); // In hoa ký tự
        }
    }

    printf("Chuoi sau khi xu ly: %s\n", str);

    return 0;
}