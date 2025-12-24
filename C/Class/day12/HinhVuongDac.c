#include <stdio.h>

void veHinhVuongDac(int canh) {
    if (canh <= 0) {
        return;
    }

    for (int i = 0; i < canh; i++) {
        for (int j = 0; j < canh; j++) {
            printf("* ");
        }
        printf("\n");
    }
}

int main() {
    veHinhVuongDac(5);
    printf("\n");
    veHinhVuongDac(4);
    return 0;
}