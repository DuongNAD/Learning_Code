#include <stdio.h>

void veTamGiacCanNguocRong(int chieuCao) {
    if (chieuCao <= 0) {
        return;
    }

    for (int i = chieuCao; i >= 1; i--) {
        for (int j = 1; j <= chieuCao - i; j++) {
            printf(" ");
        }

        for (int k = 1; k <= 2 * i - 1; k++) {
            if (i == chieuCao || k == 1 || k == 2 * i - 1) {
                printf("*");
            } else {
                printf(" ");
            }
        }
        printf("\n");
    }
}

int main() {
    veTamGiacCanNguocRong(5);
    printf("\n");
    veTamGiacCanNguocRong(6);
    return 0;
}