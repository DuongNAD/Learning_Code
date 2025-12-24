#include <stdio.h>

void veTamGiacRong(int chieuCao) {
    for (int i = 1; i <= chieuCao; i++) {
        for (int j = 1; j <= i; j++) {
            if (j == 1 || j == i || i == chieuCao) {
                printf("* ");
            } else {
                printf("  ");
            }
        }
        printf("\n");
    }
}

int main() {
    int chieuCao;
    printf("Nhap chieu cao tam giac: ");
    scanf("%d", &chieuCao);

    veTamGiacRong(chieuCao);

    return 0;
}