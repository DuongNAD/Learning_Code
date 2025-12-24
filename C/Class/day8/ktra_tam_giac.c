#include <stdio.h>

int main() {
    int angle1, angle2, angle3;
    printf("Enter three angles of a triangle: ");
    scanf("%d %d %d", &angle1, &angle2, &angle3);

    printf("\nOUTPUT:\n");
    if (angle1 > 0 && angle2 > 0 && angle3 > 0 && (angle1 + angle2 + angle3 == 180)) {
        printf("Valid Triangle\n");
    } else {
        printf("Not a Valid Triangle\n");
    }

    return 0;
}