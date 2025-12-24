#include <stdio.h>

int main() {
    int n;
    printf("Nhap so nguyen duong n: ");
    scanf("%d", &n);
    printf("Cac cap so nguyen to sinh doi nho hon %d la:\n", n);
    for (int i = 2; i < n - 2; i++) {
        if (kiemTraNguyenTo(i) && kiemTraNguyenTo(i + 2)) {
            printf("(%d, %d) ", i, i + 2);
        }
    }
    printf("\n");
    return 0;
}