#include <stdio.h>
#include <string.h>
#include <ctype.h>

int demKyTuChu(char chuoi[]) {
    int dem = 0;
    for (int i = 0; i < strlen(chuoi); i++) {
        if (isalpha(chuoi[i])) {
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

    int soKyTuChu = demKyTuChu(chuoi);
    printf("So ky tu chu trong chuoi la: %d\n", soKyTuChu);

    return 0;
}