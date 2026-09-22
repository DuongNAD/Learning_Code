#include <stdio.h>

void veHinhThoiDac(int banKinh) {
    if (banKinh <= 0) {
        return;
    }

    for (int i = 0; i < banKinh; i++) {
        for (int j = 0; j < banKinh - i - 1; j++) {
            printf(" ");
        }
        for (int j = 0; j < 2 * i + 1; j++) {
            printf("*");
        }
        printf("\n");
    }

    for (int i = banKinh - 2; i >= 0; i--) {
        for (int j = 0; j < banKinh - i - 1; j++) {
            printf(" ");
        }
        for (int j = 0; j < 2 * i + 1; j++) {
            printf("*");
        }
        printf("\n");
    }
}

int main() {
    veHinhThoiDac(5);
    printf("\n");
    veHinhThoiDac(3);
    return 0;
}