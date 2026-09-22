#include <stdio.h>

int main() {
    int num;
    printf("Enter an integer: ");
    scanf("%d", &num);

    if (num < 0) {
        num = -num;
    }

    printf("\nOUTPUT:\n");
    printf("Absolute Value: %d\n", num);

    return 0;
}