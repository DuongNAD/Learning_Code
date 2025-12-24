#include <stdio.h>

int main() {
    int chieuDai, chieuCao;

    printf("Nhap chieu dai song: ");
    scanf("%d", &chieuDai);

    printf("Nhap chieu cao song: ");
    scanf("%d", &chieuCao);

    for (int i = 0; i < chieuCao; i++) {
        for (int j = 0; j < chieuDai; j++) {
            if ((i + j) % 2 == 0) {
                printf("*");
            } else {
                printf(" ");
            }
        }
        printf("\n");
    }

    return 0;
}