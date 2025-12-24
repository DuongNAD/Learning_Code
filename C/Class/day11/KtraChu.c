#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main() {
    char s[100];
    printf("Nhap chuoi: ");
    gets(s);

    int hoa = 0, thuong = 0, so = 0, dacbiet = 0;

    for (int i = 0; i < strlen(s); i++) {
        if (isupper(s[i])) hoa++;
        else if (islower(s[i])) thuong++;
        else if (isdigit(s[i])) so++;
        else dacbiet++;
    }

    printf("Hoa=%d, Thuong=%d, So=%d, Dac biet=%d\n", hoa, thuong, so, dacbiet);
    return 0;
}