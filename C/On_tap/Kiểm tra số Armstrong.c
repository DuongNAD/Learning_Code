#include <stdio.h>
#include <math.h>

int isArmstrong(int num) {
    int originalNum = num, remainder, n = 0, result = 0;
    while (originalNum != 0) {
        originalNum /= 10;
        ++n;
    }
    originalNum = num;
    while (originalNum != 0) {
        remainder = originalNum % 10;
        result += pow(remainder, n);
        originalNum /= 10;
    }
    return result == num;
}

int main() {
    int num;
    printf("Nhap mot so: ");
    scanf("%d", &num);
    if (isArmstrong(num)) {
        printf("%d la so Armstrong.\n", num);
    } else {
        printf("%d khong phai so Armstrong.\n", num);
    }
    return 0;
}