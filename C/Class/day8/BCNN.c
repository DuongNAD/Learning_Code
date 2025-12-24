#include <stdio.h>

int main() {
    int a, b, gcd, lcm;
    printf("Enter two integers a and b: ");
    scanf("%d %d", &a, &b);

    int n1 = a, n2 = b;
    // Tìm GCD
    while (n2 != 0) {
        int temp = n2;
        n2 = n1 % n2;
        n1 = temp;
    }
    gcd = n1;
    
    // Tính LCM, kiểm tra để tránh chia cho 0
    if (gcd != 0) {
        lcm = (a * b) / gcd;
    } else {
        lcm = 0;
    }
    
    printf("\nOUTPUT:\n");
    printf("LCM: %d\n", lcm);

    return 0;
}