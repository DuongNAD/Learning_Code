#include <stdio.h>
#include <string.h>
#include <ctype.h>

int kiemTraPalindrome(char str[]) {
    int len = strlen(str);
    for (int i = 0; i < len / 2; i++) {
        if (tolower(str[i]) != tolower(str[len - i - 1])) {
            return 0;
        }
    }
    return 1;
}

int main() {
    char str[100];
    printf("Nhap chuoi: ");
    fgets(str, sizeof(str), stdin);
    if (kiemTraPalindrome(str)) {
        printf("Chuoi la palindrome.\n");
    } else