#include <stdio.h>
#include <math.h>

float dienTichHinhTron(float banKinh) {
    return M_PI * banKinh * banKinh;
}

float chuViHinhTron(float banKinh) {
    return 2 * M_PI * banKinh;
}

int main() {
    float banKinh;

    printf("Nhap ban kinh hinh tron: ");
    scanf("%f", &banKinh);

    printf("Dien tich: %.2f\n", dienTichHinhTron(banKinh));
    printf("Chu vi: %.2f\n", chuViHinhTron(banKinh));

    return 0;
}