#include <stdio.h>

void veTamGiacNguoc2(int chieuCao) {
    for (int i = chieuCao; i >= 1; i--) {
        for (int j = 1; j <= chieuCao - i; j++) {
            printf("  ");
        }
        for (int j = 1; j <= 2 * i - 1; j++) {
            printf("* ");
        }
        printf("\n");
    }
}

int main() {
    int chieuCao;
    printf("Nhap chieu cao tam