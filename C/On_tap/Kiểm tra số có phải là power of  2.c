#include <stdio.h>
#include <stdbool.h>

bool isPowerOfTwo(int n) {
    if (n <= 0) {
        return false;
    }
    return (n & (n - 1)) == 0;
}

int main() {
    int num;
    printf("Nhập một số nguyên: ");
    scanf("%d", &num);

    if (isPowerOfTwo(num)) {
        printf("%d là lũy thừa của 2.\n", num);
    } else {
        printf("%d không phải là lũy thừa của 2.\n", num);
    }

    return 0;
}