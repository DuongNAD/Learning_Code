#include <stdio.h>

int main() {
    int chieuCao;

    printf("Nhap chieu cao: ");
    scanf("%d", &chieuCao);

    for (int i = 1; i <= chieuCao; i++) {
        for (int j = 1; j <= i; j++) {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}