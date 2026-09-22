#include <stdio.h>

// Hàm tìm Ước chung lớn nhất (ƯCLN) bằng thuật toán Euclid
int tim_ucln(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// Hàm tìm Bội chung nhỏ nhất (BCNN)
int tim_bcnn(int a, int b) {
    // Công thức: BCNN(a, b) = (|a * b|) / ƯCLN(a, b)
    // Vì a và b là số nguyên dương nên |a*b| = a*b
    int ucln = tim_ucln(a, b);
    return (a * b) / ucln;
}

int main() {
    int so_a, so_b;

    // Nhập hai số nguyên dương từ người dùng
    printf("Nhap so nguyen duong a: ");
    scanf("%d", &so_a);
    printf("Nhap so nguyen duong b: ");
    scanf("%d", &so_b);

    // Đảm bảo a và b là số dương
    if (so_a <= 0 || so_b <= 0) {
        printf("Vui long nhap hai so nguyen duong.\n");
        return 1; // Thoát với mã lỗi
    }

    // Tính toán và in kết quả
    int ucln = tim_ucln(so_a, so_b);
    int bcnn = tim_bcnn(so_a, so_b);

    printf("\nƯCLN cua %d va %d la: %d\n", so_a, so_b, ucln);
    printf("BCNN cua %d va %d la: %d\n", so_a, so_b, bcnn);

    return 0;
}