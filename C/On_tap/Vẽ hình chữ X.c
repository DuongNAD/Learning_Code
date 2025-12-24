#include <stdio.h>

void drawX(int size) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            if (i == j || i + j == size - 1) {
                printf("*");
            } else {
                printf(" ");
            }
        }
        printf("\n");
    }
}

int main() {
    int size;
    printf("Nhap kich thuoc: ");
    scanf("%d", &size);
    drawX(size);
    return 0;
}