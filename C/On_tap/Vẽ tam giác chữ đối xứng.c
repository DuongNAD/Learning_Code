#include <stdio.h>

void tamGiacChuDoiXung(int chieuCao) {
    for (int i = 1; i <= chieuCao; i++) {
        char kyTu = 'A';
        for (int j = 1; j <= chieuCao - i; j++) {
            printf("  ");
        }
        for (int j = 1; j <= 2 * i - 1; j++) {
            printf("%c ", kyTu);
            if (j < i) {
                kyTu++;
            } else {
                kyTu--;
            }
        }
        printf("\n");
    }
}

int main() {
    int chieuCao;
    printf("Nhap chieu cao tam giac: ");
    scanf("%d", &chieuCao);

    tamGiacChuDoiXung(chieuCao);

    return 0;
}