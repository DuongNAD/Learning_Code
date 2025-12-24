#include <stdio.h>

void veHinhVuongRongGiua(int canh) {
    for (int i = 0; i < canh; i++) {
        for (int j = 0; j < canh; j++) {
            if (i == 0 || i == canh - 1 || j == 0 || j == canh - 1) {
                printf("* ");
            } else {
                printf("  ");
            }
        }
        printf("\n");
    }
}

int main() {
    int canh;
    printf("Nhap canh hinh vuong: ");
    scanf("%d", &canh);

    veHinhVuongRongGiua(canh);

    return 0;
}