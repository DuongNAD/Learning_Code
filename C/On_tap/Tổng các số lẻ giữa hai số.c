#include <stdio.h>

int main() {
    int x, y;
    int sum = 0;

    printf("Nhap hai so nguyen x va y: ");
    scanf("%d%d", &x, &y);

    // Ð?m b?o x < y
    if (x > y) {
        int temp = x;
        x = y;
        y = temp;
    }

    // Duy?t t? x+1 d?n y-1
    for (int i = x + 1; i < y; i++) {
        if (i % 2 != 0) {  // N?u là s? l?
            sum += i;
        }
    }

    printf("Tong cac so le nam giua %d va %d la: %d\n", x, y, sum);

    return 0;
}
