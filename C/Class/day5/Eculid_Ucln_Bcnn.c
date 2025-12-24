#include <stdio.h>
#include <math.h>

int main() {
    int a, b;
    printf("nhap a = ");
    scanf("%d",&a);
    printf("nhap b = ");
    scanf("%d",&b);
   
    // Lưu lại giá trị ban đầu của a và b
    int a_copy = a;
    int b_copy = b;

    // Thuật toán Euclid để tìm GCD
    while (b_copy != 0) {
        int temp = a_copy % b_copy;
        a_copy = b_copy;
        b_copy = temp;
    }

    // a_copy lúc này chính là GCD
    printf("gcd = %d\n", a_copy);

    // Tính và in ra LCM
    // Công thức: LCM(a, b) = (|a * b|) / GCD(a, b)
    printf("lcm = %lld", abs((long long)a * b) / a_copy);
    
    return 0; // Thêm dòng này để kết thúc hàm main đúng chuẩn
}