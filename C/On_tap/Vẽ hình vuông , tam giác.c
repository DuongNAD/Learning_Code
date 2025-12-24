#include <stdio.h>

void drawSquare(int size) {
    int i, j;
    for (i = 0; i < size; i++) {
        for (j = 0; j < size; j++) {
            printf("*");
        }
        printf("\n");
    }
}

void drawTriangle(int height) {
    int i, j;
    for (i = 1; i <= height; i++) {
        for (j = 1; j <= i; j++) {
            printf("*");
        }
        printf("\n");
    }
}

int main() {
    int choice, size;
    printf("1. Ve hinh vuong\n2. Ve hinh tam giac\nChon hinh: ");
    scanf("%d", &choice);
    printf("Nhap kich thuoc: ");
    scanf("%d", &size);
    if (choice == 1) {
        drawSquare(size);
    } else if (choice == 2) {
        drawTriangle(size);
    } else {
        printf("Lua chon khong hop le.");
    }
    return 0;
}