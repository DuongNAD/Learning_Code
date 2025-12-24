#include <stdio.h>

int main() {
    int n = 5;
    long long factorial = 1;

    for (int i = 1; i <= n; i++) {
        factorial *= i;
    }

    printf("Giai thua cua %d la: %lld\n", n, factorial);

    return 0;
}