#include <stdio.h>
#include <math.h>

float dienTichTamGiac(float a, float b, float c) {
    float p = (a + b + c) / 2;
    return sqrt(p * (p - a) * (p - b) * (p - c));
}

float chuViTamGiac(float a, float b, float c) {
    return a + b + c;
}

int main() {
    float a, b, c;

    printf("Nhap 3 canh tam giac: ");
    scanf("%f %f %f", &a, &b, &c);

    printf("Dien tich: %.2f\n", dienTichTamGiac(a, b, c));
    printf("Chu vi: %.2f\n", chuViTamGiac(a, b, c));

    return 0;
}