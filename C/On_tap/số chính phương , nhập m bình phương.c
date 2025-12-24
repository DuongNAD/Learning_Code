#include <stdio.h>
#include <math.h>

// Hàm kiểm tra xem một số có phải là số chính phương hay không
int isPerfectSquare(int n) {
    if (n < 0) {
        return 0; // Số âm không phải là số chính phương
    }
    int sqrtN = sqrt(n);
    return sqrtN * sqrtN == n;
}

// Hàm tính lũy thừa bậc M
int power(int base, int exp) {
    int result = 1;
    for (int i = 0; i < exp; i++) {
        result *= base;
    }
    return result;
}

int main() {
    int n, m;

    printf("Nhap N = ");
    scanf("%d", &n);

    int arr[n];

    printf("Nhap mang %d so nguyen:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Nhap M = ");
    scanf("%d", &m);

    printf("OUTPUT:\n");

    for (int i = 0; i < n; i++) {
        if (isPerfectSquare(arr[i])) {
            printf("%d ", power(arr[i], m));
        }
    }

    printf("\n");

    return 0;
}