#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, i = n, j = n;
    printf("Nhap so nguyen duong n: ");
    scanf("%d", &n);
    while (1) {
        if (kiemTraNguyenTo(i)) {
            printf("So nguyen to gan nhat voi %d la: %d\n", n, i);
            break;
        }
        if (kiemTraNguyenTo(j)) {
            printf("So nguyen to gan nhat voi %d la: %d\n", n, j);
            break;
        }
        i--;
        j++;
    }
    return 0;
}