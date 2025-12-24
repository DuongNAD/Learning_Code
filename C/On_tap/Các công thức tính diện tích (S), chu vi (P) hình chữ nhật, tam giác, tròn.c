#include <stdio.h>
#include <math.h>

// Hình chữ nhật
float dienTichHinhChuNhat(float chieuDai, float chieuRong) {
    return chieuDai * chieuRong;
}

float chuViHinhChuNhat(float chieuDai, float chieuRong) {
    return 2 * (chieuDai + chieuRong);
}

// Tam giác
float dienTichTamGiac(float canhDay, float chieuCao) {
    return 0.5 * canhDay * chieuCao;
}

float chuViTamGiac(float a, float b, float c) {
    return a + b + c;
}

// Hình tròn
float dienTichHinhTron(float banKinh) {
    return M_PI * banKinh * banKinh;
}

float chuViHinhTron(float banKinh) {
    return 2 * M_PI * banKinh;
}

int main() {
    // Ví dụ sử dụng
    printf("Dien tich hinh chu nhat: %.2f\n", dienTichHinhChuNhat(5, 10));
    printf("Chu vi hinh chu nhat: %.2f\n", chuViHinhChuNhat(5, 10));
    printf("Dien tich tam giac: %.2f\n", dienTichTamGiac(6, 8));
    printf("Chu vi tam giac: %.2f\n", chuViTamGiac(3, 4, 5));
    printf("Dien tich hinh tron: %.2f\n", dienTichHinhTron(7));
    printf("Chu vi hinh tron: %.2f\n", chuViHinhTron(7));

    return 0;
}