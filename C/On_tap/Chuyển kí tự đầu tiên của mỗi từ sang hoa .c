#include <stdio.h>
#include <string.h>
#include <ctype.h>

void chuyenHoaKyTuDau(char *str) {
    int i, len = strlen(str);
    int isFirstChar = 1;

    for (i = 0; i < len; i++) {
        if (isFirstChar && islower(str[i])) {
            str[i] = toupper(str[i]);
            isFirstChar = 0;
        } else if (isspace(str[i])) {
            isFirstChar = 1;
        }
    }
}

int main() {
    char str[1000];

    printf("Nhap chuoi: ");
    fgets(str, sizeof(str), stdin);

    chuyenHoaKyTuDau(str);

    printf("Chuoi sau khi chuyen doi: %s", str);

    return 0;
}