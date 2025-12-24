#include <stdio.h>

void tamGiacCanRong(int rows) {
    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= rows - i; j++) {
            printf(" ");
        }
        for (int j = 1; j <= 2 * i - 1; j++) {
            if (j == 1 || j == 2 * i - 1 || i == rows) {
                printf("*");
            } else {
                printf(" ");
            }
        }
        printf("\n");
    }
}

int main() {
    int rows;
    printf("Nhap so hang: ");
    scanf("%d", &rows);
    tamGiacCanRong(rows);
    return 0;
}