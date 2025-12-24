#include <stdio.h>
#include <ctype.h>

int demDigitTrongChuoi(char str[]) {
    int dem = 0;
    for (int i = 0; str[i] != '\0'; i++) {
        if (isdigit(str[i])) {
            dem++;
        }
    }
    return dem;
}

int main() {
    char str[] = "Hello123World456";

    printf("So luong digit trong chuoi: %d\n", demDigitTrongChuoi(str));

    return 0;
}