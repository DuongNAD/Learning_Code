#include <stdio.h>
#include <ctype.h>

int main() {
    char str[] = "This is a sample string.";
    int counts[26] = {0}; // Mảng để lưu số lần xuất hiện của mỗi chữ cái

    for (int i = 0; str[i] != '\0'; i++) {
        if (isalpha(str[i])) {
            char ch = tolower(str[i]);
            counts[ch - 'a']++;
        }
    }

    printf("Tan suat xuat hien cua cac chu cai:\n");
    for (int i = 0; i < 26; i++) {
        if (counts[i] > 0) {
            printf("%c: %d\n", 'a' + i, counts[i]);
        }
    }

    return 0;
}