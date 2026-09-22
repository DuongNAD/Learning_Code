#include <stdio.h>

int main() {
    float principal, rate, time, interest;
    printf("Enter principal, rate, and time: ");
    scanf("%f %f %f", &principal, &rate, &time);

    interest = (principal * rate * time) / 100.0f;

    printf("\nOUTPUT:\n");
    printf("Simple Interest: %.2f\n", interest);

    return 0;
}