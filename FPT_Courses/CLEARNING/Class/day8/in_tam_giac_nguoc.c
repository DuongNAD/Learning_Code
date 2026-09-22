#include <stdio.h>

int main() {
    int N, i, j;
    printf("Enter number of rows N: ");
    scanf("%d", &N);

    printf("\nOUTPUT:\n");
    for (i = N; i >= 1; i--) {
        for (j = 1; j <= i; j++) {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}