#include <stdio.h>

int main() {
    const float KM_TO_MILES = 0.621371f;
    float km, miles;
    printf("Enter kilometers: ");
    scanf("%f", &km);

    miles = km * KM_TO_MILES;

    printf("\nOUTPUT:\n");
    printf("Miles: %.2f\n", miles);

    return 0;
}