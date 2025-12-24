#include <stdio.h>

void veHinhBinhHanh(int chieuDai, int chieuCao) {
    for (int i = 1; i <= chieuCao; i++) {
        for (int j = 1; j < i; j++) {
            printf("  "); // In kho?ng tr?ng
        }
        for (int j = 1; j <= chieuDai; j++) {
            printf("* ");
        }
        printf("\n");
    }
}

int main() {
    int chieuDai, chieuCao;
    printf("Nhap chieu dai hinh binh hanh: ");
    scanf("%d", &chieuDai);
    printf("Nhap chieu cao hinh binh hanh: ");
    scanf("%d", &chieuCao);

    veHinhBinhHanh(chieuDai, chieuCao);

    return 0;
}