#include <stdio.h>
#include <math.h>

int main() {
    int n;
    printf("nhap n = ");
    scanf("%d", &n);

    int n_is_prime = 1; // Giả sử n là số nguyên tố
    if (n <= 1) {
        n_is_prime = 0;
    } else {
        for (int i = 2; i <= sqrt(n); i++) {
            if (n % i == 0) {
                n_is_prime = 0; // Nếu tìm thấy ước, không phải SNT
                break;
            }
        }
    }

    if (n_is_prime == 1) {
        printf("Yes, %d la so nguyen to.\n", n);
    } else {
        printf("No, %d khong phai la so nguyen to.\n", n);
    }

    // --- Phần 2: In ra các số nguyên tố từ 2 đến n ---
    printf("Cac so nguyen to tu 2 den %d la:\n", n);
    
    // Vòng lặp ngoài: duyệt qua từng số i từ 2 đến n
    for (int i = 2; i <= n; i++) { // <-- THAY ĐỔI Ở ĐÂY: i <= n
        int i_is_prime = 1; 

        // Vòng lặp trong: kiểm tra xem i có phải là số nguyên tố không
        for (int j = 2; j <= sqrt(i); j++) {
            if (i % j == 0) {
                i_is_prime = 0;
                break;
            }
        }

        if (i_is_prime == 1) {
            printf("%d\t", i);
        }
    }
    printf("\n");

    return 0;
}