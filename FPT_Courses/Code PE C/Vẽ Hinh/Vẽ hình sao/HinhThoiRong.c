#include <stdio.h>

void veHinhThoiRong(int banKinh) {
    if (banKinh <= 0) {
        return;
    }

    for (int i = 0; i < banKinh; i++) {
        for (int j = 0; j < banKinh - i - 1; j++) {
            printf(" ");
        }
        for (int j = 0; j < 2 * i + 1; j++) {
            if (j == 0 || j == 2 * i) {
                printf("*");
            } else {
                printf(" ");
            }
        }
        printf("\n");
    }

    for (int i = banKinh - 2; i >= 0; i--) {
        for (int j = 0; j < banKinh - i - 1; j++) {
            printf(" ");
        }
        for (int j = 0; j < 2 * i + 1; j++) {
            if (j == 0 || j == 2 * i) {
                printf("*");
            } else {
                printf(" ");
            }
        }
        printf("\n");
    }
}

int main() {
    veHinhThoiRong(5);
    printf("\n");
    veHinhThoiRong(3);
    return 0;
}