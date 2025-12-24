#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char str[100];
    printf("Nhap chuoi: ");
    gets(str);

    str[0] = toupper(str[0]);
    for (int i = 1; i < strlen(str); i++) {
        if (str[i - 1] == ' ') {
            str[i] = toupper(str[i]);
        }
    }
    printf("Chuoi sau khi xu ly: %s\n", str);
    return 0;
}