#include <stdio.h>

void veTamGiacVuongNguocRong(int chieuCao) {
    if (chieuCao <= 0) {
        return;
    }

    for (int i = 0; i < chieuCao; i++) {
        for (int j = 0; j < chieuCao - i; j++) {
            if (i == 0 || j == 0 || j == chieuCao - i - 1) {
                printf("*");
            } else {
                printf(" ");
            }
        }
        printf("\n");
    }
}

int main() {
    veTamGiacVuongNguocRong(5);
    printf("\n");
    veTamGiacVuongNguocRong(8);
    return 0;
}