#include <stdio.h>

void veTamGiacCanDac(int chieuCao) {
    if (chieuCao <= 0) {
        return;
    }

    for (int i = 1; i <= chieuCao; i++) {
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
    veTamGiacCanDac(5);
    printf("\n");
    veTamGiacCanDac(4);
    return 0;
}