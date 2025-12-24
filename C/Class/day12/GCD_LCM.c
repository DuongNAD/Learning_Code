#include <stdio.h>
#include <stdlib.h> /* De su dung ham llabs (tri tuyet doi cho long long) */

/*
 * Ham tinh Uoc chung lon nhat (GCD)
 * Su dung giai thuat Euclidean (lap)
 */
long long gcd(long long a, long long b) {
    a = llabs(a);
    b = llabs(b);

    if (a == 0 && b == 0) {
        return 0; /* GCD(0, 0) khong xac dinh, quy uoc la 0 */
    }
    if (a == 0) {
        return b;
    }
    if (b == 0) {
        return a;
    }

    while (b != 0) {
        long long temp = b;
        b = a % b;
        a = temp;
    }
    
    return a;
}

/*
 * Ham tinh Boi chung nho nhat (LCM)
 * Su dung cong thuc: LCM(a, b) = |a * b| / GCD(a, b)
 */
long long lcm(long long a, long long b) {
    if (a == 0 || b == 0) {
        return 0;
    }

    long long gcd_val = gcd(a, b);
    
    /* * Phep toan (a / gcd_val) * b giup tranh tran so 
     * so voi (a * b) / gcd_val khi a, b qua lon
     */
    return llabs((a / gcd_val) * b);
}

int main() {
    long long num1, num2;

    printf("--- CHUONG TRINH TIM GCD VA LCM ---\n");
    printf("Nhap vao so nguyen a: ");
    scanf("%lld", &num1);
    
    printf("Nhap vao so nguyen b: ");
    scanf("%lld", &num2);

    long long result_gcd = gcd(num1, num2);
    long long result_lcm = lcm(num1, num2);

    printf("\n------------------------------------\n");
    printf("So a: %lld\n", num1);
    printf("So b: %lld\n", num2);
    printf("------------------------------------\n");
    printf("Uoc chung lon nhat (GCD): %lld\n", result_gcd);
    printf("Boi chung nho nhat (LCM): %lld\n", result_lcm);

    return 0;
}