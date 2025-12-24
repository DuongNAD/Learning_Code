#include <stdio.h>

int main() {
    int n, count = 0, i = 2;
    printf("Nhap so nguyen duong n: ");
    scanf("%d", &n);
    printf("%d so nguyen to dau tien la:\n", n);
    while (count < n) {
        if (kiemTraNguyenTo(i)) {
            printf("%d ", i);
            count++;
        }
        i++;
    }
    printf("\n");
    return 0;
}