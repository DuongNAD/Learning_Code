#include <stdio.h>
#include <string.h>
#include <ctype.h>

void chuyenHoaViTriChan(char *str) {
    int i, len = strlen(str);

    for (i = 0; i < len; i++) {
        if (i % 2 == 0 && islower(str[i])) {
            str[i] = toupper(str[i]);
        }
    }
}

int main() {
    char str[1000];

    printf("Nhap chuoi: ");
    fgets(str, sizeof(str), stdin);

    chuyenHoaViTriChan(str);

    printf("Chuoi sau khi chuyen doi: %s", str);

    return 0;
}