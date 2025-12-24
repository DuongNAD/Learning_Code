#include <stdio.h>
#include <math.h>

double tinhBieuThuc(int n, double x) {
    return pow(-1, n) * pow(x, n);
}

int main() {
    int n;
    double x;

    printf("Nhap n: ");
    scanf("%d", &n);
    printf("Nhap x: ");
    scanf("%lf", &x);

    printf("Ket qua: %.2lf\n", tinhBieuThuc(n, x));

    return 0;
}