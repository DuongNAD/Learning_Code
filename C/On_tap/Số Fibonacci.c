#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool isPerfectSquare(int n) {
    int root = sqrt(n);
    return root * root == n;
}

bool isFibonacci(int n) {
    return isPerfectSquare(5 * n * n + 4) || isPerfectSquare(5 * n * n - 4);
}

int main() {
    int num;
    printf("Nhập một số nguyên: ");
    scanf("%d", &num);

    if (isFibonacci(num)) {
        printf("%d là số Fibonacci.\n", num);
    } else {
        printf("%d không phải là số Fibonacci.\n", num);
    }

    return 0;
}