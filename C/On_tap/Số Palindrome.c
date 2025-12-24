#include <stdio.h>
#include <stdbool.h>

bool isPalindrome(int n) {
    int originalN = n;
    int reversedN = 0;

    while (originalN != 0) {
        reversedN = reversedN * 10 + originalN % 10;
        originalN /= 10;
    }

    return n == reversedN;
}

int main() {
    int num;
    printf("Nhập một số nguyên: ");
    scanf("%d", &num);

    if (isPalindrome(num)) {
        printf("%d là số Palindrome.\n", num);
    } else {
        printf("%d không phải là số Palindrome.\n", num);
    }

    return 0;
}