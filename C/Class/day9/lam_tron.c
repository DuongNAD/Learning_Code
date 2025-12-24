#include <stdio.h>
#include <math.h>

int main() {
    double x, r;
    scanf("%lf %lf", &x, &r);

    double xVAT = x * (1.0 + r);

    printf("floor: %.0f\n", floor(xVAT));
    printf("ceil: %.0f\n", ceil(xVAT));
    printf("round: %.0f\n", round(xVAT));
    printf("xVAT(2dp): %.2f\n", xVAT);

    return 0;
}S