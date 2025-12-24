#include <stdio.h>

void veTamGiacNguoc1(int chieuCao) {
    for (int i = chieuCao; i >= 1; i--) {
        for (int j = 1; j <= i; j++) {
            printf("* ");
        }
        printf("\n");
    }
}

int main() {
    int chieuCao;
    printf("Nhap chieu cao tam giac: ");
    scanf("%d", &chieuCao);

    veTamGiacNguoc1(chieuCao);

    return 0;
}