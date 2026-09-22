#include <stdio.h>

void veHinhVuongRongCoCheo(int canh) {
    if (canh <= 0) {
        return;
    }

    for (int i = 0; i < canh; i++) {
        for (int j = 0; j < canh; j++) {
            if (i == 0 || i == canh - 1 || j == 0 || j == canh - 1 || i == j || i + j == canh - 1) {
                printf("* ");
            } else {
                printf("  ");
            }
        }
        printf("\n");
    }
}

int main() {
    veHinhVuongRongCoCheo(7);
    printf("\n");
    veHinhVuongRongCoCheo(8);
    return 0;
}