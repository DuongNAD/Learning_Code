#include <stdio.h>

int kiemTraFibonacci(int n) {
    int a = 0, b = 1, c;
    if (n == a || n == b) {
        return 1;
    }
    while (b <= n) {
        c = a + b;
        if (c == n) {
            return 1;
        }
        a = b;
        b = c;
    }
    return 0;
}

int main() {
    int n;
    printf("Nhap so nguyen: ");
    scanf("%d", &n);

    if (kiemTraFibonacci(n)) {
        printf("%d thuoc day Fibonacci.\n", n);
    } else {
        printf("%d khong thuoc day Fibonacci.\n", n);
    }

    return 0;
}