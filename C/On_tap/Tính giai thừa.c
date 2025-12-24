#include <stdio.h>

long long factorial(int n) {
    if (n == 0) return 1;
    return n * factorial(n - 1);
}

int main() {
    int num;
    printf("Nhap mot so: ");
    scanf("%d", &num);
    printf("Giai thua cua %d la: %lld\n", num, factorial(num));
    return 0;
}