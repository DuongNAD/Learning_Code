#include <stdio.h>

float dienTichHinhChuNhat(float chieuDai, float chieuRong) {
    return chieuDai * chieuRong;
}

float chuViHinhChuNhat(float chieuDai, float chieuRong) {
    return 2 * (chieuDai + chieuRong);
}

int main() {
    float chieuDai, chieuRong;

    printf("Nhap chieu dai: ");
    scanf("%f", &chieuDai);
    printf("Nhap chieu rong: ");
    scanf("%f", &chieuRong);

    printf("Dien tich: %.2f\n", dienTichHinhChuNhat(chieuDai, chieuRong));
    printf("Chu vi: %.2f\n", chuViHinhChuNhat(chieuDai, chieuRong));

    return 0;
}