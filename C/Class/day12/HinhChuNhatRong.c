#include <stdio.h>

void veHinhChuNhatRong(int chieuDai, int chieuRong) {
    if (chieuDai <= 0 || chieuRong <= 0) {
        return;
    }

    for (int i = 0; i < chieuRong; i++) {
        for (int j = 0; j < chieuDai; j++) {
            if (i == 0 || i == chieuRong - 1 || j == 0 || j == chieuDai - 1) {
                printf("*");
            } else {
                printf(" ");
            }
        }
        printf("\n");
    }
}

int main() {
    veHinhChuNhatRong(10, 5);
    printf("\n");
    veHinhChuNhatRong(7, 7);
    return 0;
}