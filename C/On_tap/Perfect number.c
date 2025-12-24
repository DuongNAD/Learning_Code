#include <stdio.h>

int kiemTraSoHoanHao(int n) {
    if (n <= 1) {
        return 0;
    }
    int tongUoc = 1;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            tongUoc += i;
            if (i * i != n) {
                tongUoc += n / i;
            }
        }
    }
    return tongUoc == n;
}

int main() {
    int n;
    printf("Nhap so nguyen: ");
    scanf("%d", &n);

    if (kiemTraSoHoanHao(n)) {
        printf("%d la so hoan hao.\n", n);
    } else {
        printf("%d khong phai so hoan hao.\n", n);
    }

    return 0;
}