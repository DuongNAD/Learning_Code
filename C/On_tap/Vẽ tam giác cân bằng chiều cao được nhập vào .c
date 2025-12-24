#include <stdio.h>

int main() {
    int chieuCao;

    printf("Nhap chieu cao: ");
    scanf("%d", &chieuCao);

    for (int i = 1; i <= chieuCao; i++) {
        for (int j = 1; j <= chieuCao - i; j++) {
            printf(" ");
        }
        for (int k = 1; k <= 2 * i - 1; k++) {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}