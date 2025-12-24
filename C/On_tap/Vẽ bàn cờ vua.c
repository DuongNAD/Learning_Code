#include <stdio.h>

void chessboard(int size) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            if ((i + j) % 2 == 0) {
                printf("* ");
            } else {
                printf("  ");
            }
        }
        printf("\n");
    }
}

int main() {
    int size;
    printf("Nhap kich thuoc: ");
    scanf("%d", &size);
    chessboard(size);
    return 0;
}