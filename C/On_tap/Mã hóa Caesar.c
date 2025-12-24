#include <stdio.h>
#include <ctype.h>

void caesarCipher(char *str, int shift) {
    for (int i = 0; str[i] != '\0'; i++) {
        if (isalpha(str[i])) {
            char base = islower(str[i]) ? 'a' : 'A';
            str[i] = (str[i] - base + shift) % 26 + base;
        }
    }
}

int main() {
    char str[] = "Hello, World!";
    int shift = 3;

    caesarCipher(str, shift);

    printf("Chuoi ma hoa: %s\n", str);

    return 0;
}