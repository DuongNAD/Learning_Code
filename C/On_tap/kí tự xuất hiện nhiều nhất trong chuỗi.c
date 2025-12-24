#include <stdio.h>
#include <string.h>

int main() {
    char chuoi[100];
    int demKyTu[256] = {0};
    int maxDem = 0;
    char kyTuMax = '\0';

    printf("Nhap chuoi: ");
    fgets(chuoi, sizeof(chuoi), stdin);

    // Loại bỏ ký tự newline nếu có
    if (chuoi[strlen(chuoi) - 1] == '\n') {
        chuoi[strlen(chuoi) - 1] = '\0';
    }

    // Đếm số lần xuất hiện của từng ký tự
    for (int i = 0; i < strlen(chuoi); i++) {
        demKyTu[(unsigned char)chuoi[i]]++;
    }

    // Tìm ký tự xuất hiện nhiều nhất
    for (int i = 0; i < 256; i++) {
        if (demKyTu[i] > maxDem) {
            maxDem = demKyTu[i];
            kyTuMax = (char)i;
        }
    }

    printf("Ky tu xuat hien nhieu nhat la '%c' voi %d lan.\n", kyTuMax, maxDem);

    return 0;
}