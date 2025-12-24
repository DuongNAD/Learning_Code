#include <stdio.h>
#include <ctype.h>

int main() {
    char ch;
    printf("Enter a character: ");
    scanf(" %c", &ch);

    printf("\nOUTPUT:\n");
    if (isalpha(ch)) {
        printf("Alphabet\n");
    } else if (isdigit(ch)) {
        printf("Digit\n");
    } else {
        printf("Special Character\n");
    }

    return 0;
}