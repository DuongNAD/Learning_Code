#include <stdio.h>
#include <string.h>

int main() {
    char str[100], c;
    int count = 0;
    printf("Nhap chuoi: ");
    gets(str);
    printf("Nhap ky tu: ");
    scanf("%c", &c);

    for (int i = 0; i < strlen(str); i++) {
        if (str[i] == c) count++;
    }
    printf("So lan xuat hien: %d\n", count);
    return 0;
}