#include <stdio.h>
#include <string.h>

void daoNguocChuoi(char str[]) {
    int len = strlen(str);
    for (int i = 0; i < len / 2; i++) {
        char temp = str[i];
        str[i] = str[len - i - 1];
        str[len - i - 1] = temp;
    }
}

int main() {
    char str[100];
    printf("Nhap chuoi: ");
    fgets(str, sizeof(str), stdin);
    daoNguocChuoi(str);
    printf("Chuoi sau khi dao nguoc: %s", str);
    return 0;
}