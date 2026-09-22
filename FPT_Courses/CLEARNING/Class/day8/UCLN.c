#include <stdio.h>

int main() {
    int a, b;
    printf("Enter two integers a and b: ");
    scanf("%d %d", &a, &b);

    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }

    printf("\nOUTPUT:\n");
    printf("GCD: %d\n", a);

    return 0;
}