#include <stdio.h>
#include <string.h>
#include <ctype.h>

void chuyenChuoiThanhThuong(char str[]) {
    for (int i = 0; str[i] != '\0'; i++) {
        str[i] = tolower(str[i]);
    }
}

int main() {
    char str[100];
    printf("Nhap chuoi: ");
    fgets(str, sizeof(str), stdin);
    chuyenChuoiThanhThuong(str);
    printf("Chuoi sau khi chuyen thanh chu thuong: %s", str);
    return 0;
}