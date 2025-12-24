#include <stdio.h>
#include <ctype.h>

void inKyTuLaChu(char str[]) {
    for (int i = 0; str[i] != '\0'; i++) {
        if (isalpha(str[i])) {
            printf("%c", str[i]);
        }
    }
    printf("\n");
}

int main() {
    char str[] = "Hello123World!";

    inKyTuLaChu(str);

    return 0;
}