#include <stdio.h>

void veHinhVuongRong(int canh) {
    if (canh <= 0) {
        return;
    }

    for (int i = 0; i < canh; i++) {
        for (int j = 0; j < canh; j++) {
            if (i == 0 || i == canh - 1 || j == 0 || j == canh - 1) {
                printf("* ");
            } else {
                printf("  ");
            }
        }
        printf("\n");
    }
}

int main() {
    veHinhVuongRong(5);
    printf("\n");
    veHinhVuongRong(6);
    return 0;
}