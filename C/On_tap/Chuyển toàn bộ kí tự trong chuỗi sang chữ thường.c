#include <stdio.h>
#include <string.h>
#include <ctype.h>

void chuyenThuongToanBo(char *str) {
    int i, len = strlen(str);

    for (i = 0; i < len; i++) {
        if (isupper(str[i])) {
            str[i] = tolower(str[i]);
        }
    }
}

int main() {
    char str[1000];

    printf("Nhap chuoi: ");
    fgets(str, sizeof(str), stdin);

    chuyenThuongToanBo(str);

    printf("Chuoi sau khi chuyen doi: %s", str);

    return 0;
}