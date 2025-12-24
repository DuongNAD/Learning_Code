#include <stdio.h>

int main() {
    const float INCH_TO_CM = 2.54f;
    float inches, cm;
    printf("Enter inches: ");
    scanf("%f", &inches);

    cm = inches * INCH_TO_CM;

    printf("\nOUTPUT:\n");
    printf("Centimeters: %.2f\n", cm);

    return 0;
}