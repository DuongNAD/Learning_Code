#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void binaryToOctal(char binary[]) {
    int len = strlen(binary);
    int octal = 0, base = 1;

    for (int i = len - 1; i >= 0; i--) {
        octal += (binary[i] - '0') * base;
        if (i % 3 == 0 || i == 0) {
            printf("%d", octal);
            octal = 0;
            base = 1;
        } else {
            base *= 2;
        }
    }
    printf("\n");
}

int main() {
    char binary[] = "101101";

    printf("Octal: ");
    binaryToOctal(binary);

    return 0;
}