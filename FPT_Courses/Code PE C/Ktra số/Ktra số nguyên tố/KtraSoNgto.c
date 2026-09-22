#include <stdio.h>
#include <stdbool.h>
#include <math.h>

/**
 * @brief Kiem tra mot so co phai la so nguyen to hay khong.
 * * @param n So nguyen can kiem tra.
 * @return true Neu n la so nguyen to.
 * @return false Neu n khong phai la so nguyen to.
 */
bool isPrime(int n) {
    // 1. Truong hop dac biet: cac so <= 1 khong phai la so nguyen to.
    if (n <= 1) {
        return false;
    }
    
    // 2. Kiem tra tinh chia het tu 2 den can bac hai cua n.
    // Chi can kiem tra den sqrt(n) de tiet kiem thoi gian.
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            return false; // Tim thay uoc so, khong phai so nguyen to.
        }
    }
    
    // 3. Neu khong tim thay uoc so nao, thi no la so nguyen to.
    return true;
}

int main() {
    int number;
    printf("Nhap mot so nguyen duong de kiem tra: ");
    scanf("%d", &number);

    if (isPrime(number)) {
        printf("%d la so nguyen to.\n", number);
    } else {
        printf("%d KHONG phai la so nguyen to.\n", number);
    }

    return 0;
}