#include <stdio.h>

void veTamGiacCanNguocDac(int chieuCao) {
    if (chieuCao <= 0) {
        return;
    }

    for (int i = chieuCao; i >= 1; i--) {
        for (int j = 1; j <= chieuCao - i; j++) {
            printf(" ");
        }

        for (int k = 1; k <= 2 * i - 1; k++) {
            printf("*");
        }
        printf("\n");
    }
}

int main() {
    veTamGiacCanNguocDac(5);
    printf("\n");
    veTamGiacCanNguocDac(4);
    return 0;
}