#include <stdio.h>

void veBanCo(int canh) {
    if (canh <= 0) {
        return;
    }

    for (int i = 0; i < canh; i++) {
        for (int j = 0; j < canh; j++) {
            if ((i + j) % 2 == 0) {
                printf("* ");
            } else {
                printf("# ");
            }
        }
        printf("\n");
    }
}

int main() {
    veBanCo(6);
    printf("\n");
    veBanCo(5);
    return 0;
}