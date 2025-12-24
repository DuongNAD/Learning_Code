#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* binaryToHex(char binary[]) {
    int len = strlen(binary);
    int hexLen = (len + 3) / 4;
    char* hex = (char*)malloc(hexLen + 1);
    hex[hexLen] = '\0';

    int hexIndex = hexLen - 1;
    int binaryIndex = len - 1;

    while (binaryIndex >= 0) {
        int value = 0;
        for (int i = 0; i < 4 && binaryIndex >= 0; i++) {
            if (binary[binaryIndex] == '1') {
                value += 1 << i;
            }
            binaryIndex--;
        }

        if (value < 10) {
            hex[hexIndex] = value + '0';
        } else {
            hex[hexIndex] = value - 10 + 'A';
        }
        hexIndex--;
    }

    return hex;
}

int main() {
    char binary[100];
    printf("Nhap so nhi phan: ");
    scanf("%s", binary);

    char* hex = binaryToHex(binary);
    printf("So thap luc phan: %s\n", hex);

    free(hex);
    return 0;
}