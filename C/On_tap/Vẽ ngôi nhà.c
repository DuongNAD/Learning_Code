#include <stdio.h>

void veNgoiNha(int chieuCao) {
    // Vẽ mái nhà (tam giác cân)
    for (int i = 1; i <= chieuCao; i++) {
        for (int j = 1; j <= chieuCao - i; j++) {
            printf(" ");
        }
        for (int j = 1; j <= 2 * i - 1; j++) {
            printf("*");
        }
        printf("\n");
    }

    // Vẽ thân nhà (hình chữ nhật)
    for (int i = 1; i <= chieuCao; i++) {
        for (int j = 1; j <= 2 * chieuCao - 1; j++) {
            printf("*");
        }
        printf("\n");
    }
}

int main() {
    int chieuCao;
    printf("Nhap chieu cao ngoi nha: ");
    scanf("%d", &chieuCao);

    veNgoiNha(chieuCao);

    return 0;
}