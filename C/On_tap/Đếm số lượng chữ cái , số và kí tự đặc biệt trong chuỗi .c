#include <stdio.h>
#include <string.h>
#include <ctype.h>

void demKyTu(char str[]) {
    int chuCai = 0, chuSo = 0, kyTuDacBiet = 0;
    for (int i = 0; str[i] != '\0'; i++) {
        if (isalpha(str[i])) {
            chuCai++;
        } else if (isdigit(str[i])) {
            chuSo++;
        } else {
            kyTuDacBiet++;
        }
    }
    printf("So chu cai: %d\n", chuCai);
    printf("So chu so: %d\n", chuSo);
    printf("So ky tu dac biet: %d\n", kyTuDacBiet);
}

int main() {
    char str[100];
    printf("Nhap chuoi: ");
    fgets(str, sizeof(str), stdin);
    demKyTu(str);
    return 0;
}