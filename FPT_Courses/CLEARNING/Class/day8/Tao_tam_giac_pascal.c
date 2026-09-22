#include <stdio.h>

int main() {
    int N, i, j;
    printf("Enter number of rows N: ");
    scanf("%d", &N);

    printf("\nOUTPUT:\n");
    for (i = 0; i < N; i++) {
        int coef = 1;
        // In khoảng trắng đầu dòng
        for (j = 0; j < N - i - 1; j++) {
            printf("  "); // In 2 khoảng trắng để cân đối
        }
        for (j = 0; j <= i; j++) {
            printf("%4d", coef); // In số với độ rộng 4
            coef = coef * (i - j) / (j + 1);
        }
        printf("\n");
    }

    return 0;
}