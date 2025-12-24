#include <stdio.h>

void veHinhThoi(int chieuCao) {
    // Vẽ nửa trên hình thoi
    for (int i = 1; i <= chieuCao; i++) {
        for (int j = 1; j <= chieuCao - i; j++) {
            printf(" ");
        }
        for (int j = 1; j <= 2 * i - 1; j++) {
            printf("*");
        }
        printf("\n");
    }

    // Vẽ nửa dưới hình thoi
    for (int i = chieuCao - 1; i >= 1; i--) {
        for (int j = 1; j <= chieuCao - i; j++) {
            printf(" ");
        }
        for (int j = 1; j <= 2 * i - 1; j++) {
            printf("*");
        }
        printf("\n");
    }
}

int main() {
    int chieuCao;
    printf("Nhap chieu cao hinh thoi: ");
    scanf("%d", &chieuCao);

    veHinhThoi(chieuCao);

    return 0;
}