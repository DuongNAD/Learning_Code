#include <stdio.h>

int isPalindrome(int num) {
    int originalNum = num, reversedNum = 0, remainder;
    while (originalNum != 0) {
        remainder = originalNum % 10;
        reversedNum = reversedNum * 10 + remainder;
        originalNum /= 10;
    }
    return num == reversedNum;
}

int main() {
    int num;
    printf("Nhap mot so: ");
    scanf("%d", &num);
    if (isPalindrome(num)) {
        printf("%d la so Palindrome.\n", num);
    } else {
        printf("%d khong phai so Palindrome.\n", num);
    }
    return 0;
}