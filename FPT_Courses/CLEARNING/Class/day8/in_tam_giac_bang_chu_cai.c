#include <stdio.h>

int main() {
    int N, i, j;
    printf("Enter number of rows N: ");
    scanf("%d", &N);

    printf("\nOUTPUT:\n");
    for (i = 0; i < N; i++) {
        for (j = 0; j <= i; j++) {
            printf("%c", 'A' + j);
        }
        printf("\n");
    }

    return 0;
}