#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int hexToDecimal(char hex[]) {
    int len = strlen(hex);
    int decimal = 0;
    int base = 1;

    for (int i = len - 1; i >= 0; i--) {
        int value;
        if (hex[i] >= '0' && hex[i] <= '9') {
            value = hex[i] - '0';
        } else {
            value = hex[i] - 'A' + 10;
        }

        decimal += value * base;
        base *= 16;
    }

    return decimal;
}

int main() {
    char hex[100];
    printf("Nhap so thap luc phan: ");
    scanf("%s", hex);

    int decimal = hexToDecimal(hex);
    printf("So thap phan: %d\n", decimal);

    return 0;
}