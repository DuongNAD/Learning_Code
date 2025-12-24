#include <stdio.h>

int main() {
    int rows;
    char ch = 'A';

    printf("Enter number of rows: ");
    scanf("%d", &rows);

    if (rows <= 0) {
        printf("Number of rows must be greater than 0.\n");
        return 1;
    }

    printf("OUTPUT:\n");

    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%c ", ch);
            ch++;
        }
        printf("\n");
    }

    return 0;
}
