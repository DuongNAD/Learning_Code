#include <stdio.h>

int main() {
    int n = 10;
    int sum = 0;

    for (int i = 1; i <= n; i++) {
        sum += i;
    }

    printf("Tong tu 1 den %d la: %d\n", n, sum);

    return 0;
}