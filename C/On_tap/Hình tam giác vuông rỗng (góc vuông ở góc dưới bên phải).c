#include <stdio.h>

void tamGiacVuongRong3(int rows) {
    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= rows - i; j++) {
            printf(" ");
        }
        for (int j = 1; j <= i; j++) {
            if (j == 1 || j == i || i == rows) {
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
    tamGiacVuongRong3(rows);
    return 0;
}