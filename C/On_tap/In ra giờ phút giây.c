#include <stdio.h>

void inGioPhutGiay(int giay) {
    int gio = giay / 3600;
    int phut = (giay % 3600) / 60;
    int giayConLai = giay % 60;

    printf("Gio: %d, Phut: %d, Giay: %d\n", gio, phut, giayConLai);
}

int main() {
    int giay;
    printf("Nhap so giay: ");
    scanf("%d", &giay);

    inGioPhutGiay(giay);

    return 0;
}