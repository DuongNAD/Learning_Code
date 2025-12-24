#include <stdio.h>

void tamGiacVuong1(int rows) {
    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= i; j++) {
            printf("*");
        }
        printf("\n");
    }
}

int main() {
    int rows;
    printf("Nhap so hang: ");
    scanf("%d", &rows);
    tamGiacVuong1(rows);
    return 0;
}