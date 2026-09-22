#include <stdio.h>
#include <math.h>

int main() {
    int num, originalNum, remainder, n = 0;
    double result = 0.0;
    printf("Enter an integer: ");
    scanf("%d", &num);
    originalNum = num;

    // Đếm số chữ số
    int temp = num;
    if (temp == 0) {
        n = 1;
    } else {
        while (temp != 0) {
            temp /= 10;
            ++n;
        }
    }
    
    temp = originalNum;
    // Tính tổng lũy thừa
    while (temp != 0) {
        remainder = temp % 10;
        result += pow(remainder, n);
        temp /= 10;
    }

    printf("\nOUTPUT:\n");
    if ((int)result == originalNum) {
        printf("Armstrong Number\n");
    } else {
        printf("Not an Armstrong Number\n");
    }

    return 0;
}