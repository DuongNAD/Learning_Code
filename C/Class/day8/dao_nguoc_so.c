#include <stdio.h>

int main() {
    int num, reversed = 0, remainder;
    printf("Enter a number: ");
    scanf("%d", &num);

    int temp = num;
    while (temp != 0) {
        remainder = temp % 10;
        reversed = reversed * 10 + remainder;
        temp /= 10;
    }

    printf("\nOUTPUT:\n");
    printf("Reversed number: %d\n", reversed);

    return 0;
}