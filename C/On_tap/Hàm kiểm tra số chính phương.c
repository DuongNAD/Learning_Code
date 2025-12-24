#include <stdio.h>
#include <math.h>

int kiemTraChinhPhuong(int n) {
    if (n < 0) {
        return 0;
    }
    int canBacHai = sqrt(n);
    if (canBacHai * canBacHai == n) {
        return 1;
    }
    return 0;
}

int main() {
    int n;
    printf("Nhap so nguyen: ");
    scanf("%d", &n);

    if (kiemTraChinhPhuong(n)) {
        printf("%d la so chinh phuong.\n", n);
    } else {
        printf("%d khong phai so chinh phuong.\n", n);
    }

    return 0;
}