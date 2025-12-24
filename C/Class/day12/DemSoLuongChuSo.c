#include <stdio.h>

int main() {
    long long n;
    int count = 0;

    printf("Nhap vao mot so nguyen: ");
    scanf("%lld", &n);

    if (n == 0) {
        count = 1;
    } else {
        if (n < 0) {
            n = -n;
        }

        while (n != 0) {
            n = n / 10;
            count++;
        }
    }

    printf("So luong chu so: %d\n", count);

    return 0;
}