#include <stdio.h>
#include <string.h>
#include <ctype.h>

int demKhoangTrang(char chuoi[]) {
    int dem = 0;
    for (int i = 0; i < strlen(chuoi); i++) {
        if (isspace(chuoi[i])) {
            dem++;
        }
    }
    return dem;
}

int main() {
    char chuoi[100];

    printf("Nhap chuoi: ");
    fgets(chuoi, sizeof(chuoi), stdin);

    // Loại bỏ ký tự newline nếu có
    if (chuoi[strlen(chuoi) - 1] == '\n') {
        chuoi[strlen(chuoi) - 1] = '\0';
    }

    int soKhoangTrang = demKhoangTrang(chuoi);
    printf("So khoang trang trong chuoi la: %d\n", soKhoangTrang);

    return 0;
}