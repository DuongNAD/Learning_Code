#include <stdio.h>

int main() {
    int chieuDai, chieuRong;

    printf("Nhap chieu dai: ");
    scanf("%d", &chieuDai);

    printf("Nhap chieu rong: ");
    scanf("%d", &chieuRong);

    for (int i = 0; i < chieuRong; i++) {
        for (int j = 0; j < chieuDai; j++) {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}