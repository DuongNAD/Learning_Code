#include <stdio.h>

// Hàm tính ước chung lớn nhất (GCD) bằng thuật toán Euclid
int ucln(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    int a, b;

    printf("Nhap hai so nguyen a va b: ");
    scanf("%d%d", &a, &b);

    // Đảm bảo a và b là số dương
    if (a <= 0 || b <= 0) {
        printf("Vui long nhap hai so nguyen duong!\n");
        return 1;
    }

    int ketqua = ucln(a, b);

    printf("Uoc chung lon nhat cua %d va %d la: %d\n", a, b, ketqua);

    return 0;
}
