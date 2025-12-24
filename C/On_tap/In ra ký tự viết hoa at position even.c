#include <stdio.h>
#include <ctype.h>

void inKyTuVietHoaViTriChan(char str[]) {
    for (int i = 0; str[i] != '\0'; i++) {
        if (i % 2 == 0 && isupper(str[i])) {
            printf("%c", str[i]);
        }
    }
    printf("\n");
}

int main() {
    char str[] = "HeLlO wOrLd";

    inKyTuVietHoaViTriChan(str);

    return 0;
}