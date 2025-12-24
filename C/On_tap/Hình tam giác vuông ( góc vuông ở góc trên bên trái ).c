#include <stdio.h>

void tamGiacVuong2(int rows) {
    for (int i = rows; i >= 1; i--) {
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
    tamGiacVuong2(rows);
    return 0;
}