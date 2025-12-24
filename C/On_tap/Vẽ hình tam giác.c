#include <stdio.h>

void veTamGiac(int chieuCao) {
    for (int i = 1; i <= chieuCao; i++) {
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

    veTamGiac(chieuCao);

    return 0;
}