#include <stdio.h>
#include <string.h>
#include <ctype.h>

int demKyTuInThuong(char chuoi[]) {
    int dem = 0;
    for (int i = 0; i < strlen(chuoi); i++) {
        if (islower(chuoi[i])) {
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

    int soKyTuInThuong = demKyTuInThuong(chuoi);
    printf("So ky tu in thuong trong chuoi la: %d\n", soKyTuInThuong);

    return 0;
}