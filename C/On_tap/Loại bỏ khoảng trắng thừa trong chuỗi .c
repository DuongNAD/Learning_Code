#include <stdio.h>
#include <string.h>

void loaiBoKhoangTrangThua(char str[]) {
    int i, j = 0;
    for (i = 0; str[i] != '\0'; i++) {
        if (str[i] != ' ' || (i > 0 && str[i - 1] != ' ')) {
            str[j++] = str[i];
        }
    }
    str[j] = '\0';
}

int main() {
    char str[100];
    printf("Nhap chuoi: ");
    fgets(str, sizeof(str), stdin);
    loaiBoKhoangTrangThua(str);
    printf("Chuoi sau khi loai bo khoang trang thua: %s", str);
    return 0;
}