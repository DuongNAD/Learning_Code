#include <stdio.h>
#include <stdbool.h>

bool isPerfectNumber(int n) {
    if (n <= 1) {
        return false;
    }

    int sum = 1; // 1 luôn là ước số
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            sum += i;
            if (i * i != n) { // Tránh cộng ước số trùng lặp
                sum += n / i;
            }
        }
    }

    return sum == n;
}

int main() {
    int num;
    printf("Nhập một số nguyên: ");
    scanf("%d", &num);

    if (isPerfectNumber(num)) {
        printf("%d là số hoàn hảo.\n", num);
    } else {
        printf("%d không phải là số hoàn hảo.\n", num);
    }

    return 0;
}