#include <stdio.h>

int main() {
    int num, originalNum, reversed = 0, remainder;
    printf("Enter a number: ");
    scanf("%d", &num);
    originalNum = num;

    while (num > 0) {
        remainder = num % 10;
        reversed = reversed * 10 + remainder;
        num /= 10;
    }

    printf("\nOUTPUT:\n");
    if (originalNum == reversed) {
        printf("Palindrome Number\n");
    } else {
        printf("Not a Palindrome Number\n");
    }

    return 0;
}