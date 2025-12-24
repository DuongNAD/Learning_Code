#include <stdio.h>

int tinhDoDaiChuoi(char str[]) {
    int doDai = 0;
    while (str[doDai] != '\0') {
        doDai++;
    }
    return doDai;
}

int main() {
    char str[] = "Hello, world!";

    printf("Do dai chuoi: %d\n", tinhDoDaiChuoi(str));

    return 0;
}