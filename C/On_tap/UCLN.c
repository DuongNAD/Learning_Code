#include <stdio.h>

// Hàm tính ước chung lớn nhất dùng thuật toán Euclid
int ucln(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    int x, y;

    // Nhập hai số nguyên
    printf("Nhap so thu nhat: ");
    scanf("%d", &x);
    printf("Nhap so thu hai: ");
    scanf("%d", &y);

    // Tính và in ƯCLN
    int ketqua = ucln(x, y);
    printf("Uoc chung lon nhat cua %d va %d la: %d\n", x, y, ketqua);

    return 0;
}
