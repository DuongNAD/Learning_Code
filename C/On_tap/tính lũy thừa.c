#include <stdio.h>
#include <math.h>

int main() {
    double base = 2.0;
    double exponent = 3.0;
    double result = pow(base, exponent);

    printf("%.2lf ^ %.2lf = %.2lf\n", base, exponent, result);

    return 0;
}