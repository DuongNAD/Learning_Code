#include <stdio.h>

int main() {
    int chieuCao;

    printf("Nhap chieu cao mui ten: ");
    scanf("%d", &chieuCao);

    for (int i = 0; i < chieuCao - 1; i++) {
        for (int j = 0; j < chieuCao - i - 1; j++) {
            printf(" ");
        }
        printf("*\n");
    }

    for(int i = 0; i < chieuCao*2 -1; i++){
        printf("*");
    }
    printf("\n");

    return 0;
}