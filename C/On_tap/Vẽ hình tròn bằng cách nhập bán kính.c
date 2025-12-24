#include <stdio.h>
#include <math.h>

int main() {
    int banKinh;

    printf("Nhap ban kinh: ");
    scanf("%d", &banKinh);

    for (int y = -banKinh; y <= banKinh; y++) {
        for (int x = -banKinh; x <= banKinh; x++) {
            if (x * x + y * y <= banKinh * banKinh) {
                printf("*");
            } else {
                printf(" ");
            }
        }
        printf("\n");
    }

    return 0;
}