#include <stdio.h>

void tamGiacCoSo1(int chieuCao) {
    for (int i = 1; i <= chieuCao; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%d ", j);
        }
        printf("\n");
    }
}

int main() {
    int chieuCao;
    printf("Nhap chieu cao tam giac: ");
    scanf("%d", &chieuCao);

    tamGiacCoSo1(chieuCao);

    return 0;
}