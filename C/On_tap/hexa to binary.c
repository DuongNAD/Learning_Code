#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* hexToBinary(char hex[]) {
    int len = strlen(hex);
    char* binary = (char*)malloc(len * 4 + 1);
    binary[0] = '\0';

    for (int i = 0; i < len; i++) {
        int value;
        if (hex[i] >= '0' && hex[i] <= '9') {
            value = hex[i] - '0';
        } else {
            value = hex[i] - 'A' + 10;
        }

        for (int j = 3; j >= 0; j--) {
            if (value & (1 << j)) {
                strcat(binary, "1");
            } else {
                strcat(binary, "0");
            }
        }
    }

    return binary;
}

int main() {
    char hex[100];
    printf("Nhap so thap luc phan: ");
    scanf("%s", hex);

    char* binary = hexToBinary(hex);
    printf("So nhi phan: %s\n", binary);

    free(binary);
    return 0;
}