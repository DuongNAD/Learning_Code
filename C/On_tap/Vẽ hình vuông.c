#include <stdio.h>

void veHinhVuong(int canh) {
    for (int i = 0; i < canh; i++) {
        for (int j = 0; j < canh; j++) {
            printf("* ");
        }
        printf("\n");
    }
}

int main() {
    int canh;
    printf("Nhap canh hinh vuong: ");
    scanf("%d", &canh);

    veHinhVuong(canh);

    return 0;
}