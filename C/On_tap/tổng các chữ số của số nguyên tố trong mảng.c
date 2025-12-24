#include <stdio.h>
#include <math.h>
#include <stdbool.h>

// Hàm kiểm tra xem một số có phải là số nguyên tố hay không
bool laSoNguyenTo(int n) {
    if (n <= 1) {
        return false;
    }
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

// Hàm tính tổng các chữ số của một số
int tongChuSo(int n) {
    int tong = 0;
    while (n > 0) {
        tong += n % 10;
        n /= 10;
    }
    return tong;
}

int main() {
    int n, k;

    printf("Nhap N = ");
    scanf("%d", &n);

    int arr[n];

    printf("Nhap mang %d so nguyen:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Nhap K = ");
    scanf("%d", &k);

    printf("OUTPUT:\n");

    for (int i = 0; i < n; i++) {
        if (laSoNguyenTo(arr[i])) {
            printf("%d ", tongChuSo(arr[i]));
        }
    }

    printf("\n");

    return 0;
}