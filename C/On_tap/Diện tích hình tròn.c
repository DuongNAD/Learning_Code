#include <stdio.h>
#include <math.h>

float dienTichHinhTron(float banKinh) {
    return M_PI * banKinh * banKinh;
}

int main() {
    float banKinh;
    printf("Nhap ban kinh hinh tron: ");
    scanf("%f", &banKinh);

    printf("Dien tich hinh tron: %.2f\n", dienTichHinhTron(banKinh));

    return 0;
}