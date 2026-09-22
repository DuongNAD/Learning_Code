#include <stdio.h>

int main() {
    int N, i, j, k;
    printf("Enter number of rows N: ");
    scanf("%d", &N);

    printf("\nOUTPUT:\n");
    for (i = 1; i <= N; i++) {
        // In khoảng trắng
        for (j = 1; j <= N - i; j++) {
            printf(" ");
        }
        // In dấu sao
        for (k = 1; k <= (2 * i - 1); k++) {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}