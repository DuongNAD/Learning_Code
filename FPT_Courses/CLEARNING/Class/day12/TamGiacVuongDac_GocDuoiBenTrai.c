#include <stdio.h>

void veTamGiacVuongDac(int chieuCao) {
    if (chieuCao <= 0) {
        return;
    }

    for (int i = 1; i <= chieuCao; i++) {
        for (int j = 1; j <= i; j++) {
            printf("*");
        }
        printf("\n");
    }
}

int main() {
    veTamGiacVuongDac(5);
    printf("\n");
    veTamGiacVuongDac(7);
    return 0;
}