#include <stdio.h>
#include <math.h>

int main() {
    float radius, height, volume;
    printf("Enter radius and height: ");
    scanf("%f %f", &radius, &height);

    volume = M_PI * radius * radius * height;

    printf("\nOUTPUT:\n");
    printf("Volume: %.2f\n", volume);

    return 0;
}