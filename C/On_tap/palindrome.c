#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool isPalindrome(char *str) {
    int length = strlen(str);
    for (int i = 0, j = length - 1; i < j; i++, j--) {
        if (str[i] != str[j]) {
            return false;
        }
    }
    return true;
}

int main() {
    char str[] = "madam";
    if (isPalindrome(str)) {
        printf("Chuỗi là palindrome.\n");
    } else {
        printf("Chuỗi không là palindrome.\n");
    }
    return 0;
}