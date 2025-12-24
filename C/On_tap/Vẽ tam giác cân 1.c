#include <stdio.h>

void veTamGiacCan1(int chieuCao) {
    for (int i = 1; i <= chieuCao; i++) {
        for (int j = 1; j <= chieuCao - i; j++) {
            printf("  "); // In kho?ng tr?ng
        }
        for (int j = 1; j <= 2 * i - 1; j++) {
            printf("* ");
        }
        printf("\n");
    }
}

int main() {
    int chieuCao;
    printf("Nhap chieu cao tam giac can: ");
    scanf("%d", &chieuCao);

    veTamGiacCan1(chieuCao);

    return 0;
}