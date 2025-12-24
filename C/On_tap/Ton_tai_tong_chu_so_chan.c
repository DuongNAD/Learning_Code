#include <stdio.h>

int sumDigits(int n) {
    int sum = 0;
    n = (n < 0) ? -n : n;
    while (n) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int main() {
    int n, found = 0;
    scanf("%d", &n);
    int a[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
        if (sumDigits(a[i]) % 2 == 0) {
            found = 1;
            break;
        }
    }

    if (found)
        printf("Co so co tong chu so la chan");
    else
        printf("Khong co so nao co tong chu so chan");

    return 0;
}
