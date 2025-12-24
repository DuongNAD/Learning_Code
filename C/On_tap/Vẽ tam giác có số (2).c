#include <stdio.h>

void tamGiacCoSo2(int chieuCao) {
    int so = 1;
    for (int i = 1; i <= chieuCao; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%d ", so++);
        }
        printf("\n");
    }
}

int main() {
    int chieuCao;
    printf("Nhap chieu cao tam giac: ");
    scanf("%d", &chieuCao);

    tamGiacCoSo2(chieuCao);

    return 0;
}