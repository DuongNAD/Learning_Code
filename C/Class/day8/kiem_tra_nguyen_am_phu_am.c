#include <stdio.h>
#include <ctype.h>

int main() {
    char ch;
    printf("Enter an alphabet: ");
    scanf(" %c", &ch);

    printf("\nOUTPUT:\n");
    switch (tolower(ch)) { // Chuyển về chữ thường để xử lý một lần
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
            printf("Vowel\n");
            break;
        default:
            if (isalpha(ch)) { // Kiểm tra có phải là chữ cái không
                printf("Consonant\n");
            } else {
                printf("Not an alphabet\n");
            }
    }

    return 0;
}