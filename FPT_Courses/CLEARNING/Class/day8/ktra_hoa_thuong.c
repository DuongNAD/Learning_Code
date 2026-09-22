#include <stdio.h>
#include <ctype.h>

int main() {
    char ch;
    printf("Enter a character: ");
    scanf(" %c", &ch);

    printf("\nOUTPUT:\n");
    if (isupper(ch)) {
        printf("Uppercase Letter\n");
    } else if (islower(ch)) {
        printf("Lowercase Letter\n");
    } else {
        printf("Not a letter\n");
    }

    return 0;
}