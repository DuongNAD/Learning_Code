#include <stdio.h>
#include <string.h>

int main() {
    char chuoi[100];

    printf("Nhap chuoi: ");
    fgets(chuoi, sizeof(chuoi), stdin);

    // Loại bỏ ký tự newline nếu có
    if (chuoi[strlen(chuoi) - 1] == '\n') {
        chuoi[strlen(chuoi) - 1] = '\0';
    }

    printf("Cac ky tu trong chuoi la:\n");
    for (int i = 0; i < strlen(chuoi); i++) {
        printf("%c\n", chuoi[i]);
    }

    return 0;
}