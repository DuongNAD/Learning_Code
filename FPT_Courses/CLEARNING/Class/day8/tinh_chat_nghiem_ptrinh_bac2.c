#include <stdio.h>
#include <math.h>

int main() {
    float a, b, c, discriminant;
    printf("Enter coefficients a, b, c: ");
    scanf("%f %f %f", &a, &b, &c);

    discriminant = (b * b) - (4 * a * c);

    printf("\nOUTPUT:\n");
    if (discriminant > 0) {
        printf("Real and Distinct Roots\n");
    } else if (discriminant == 0) {
        printf("Real and Equal Roots\n");
    } else {
        printf("Complex Roots\n");
    }

    return 0;
}