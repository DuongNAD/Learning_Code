#include <stdio.h>
#include <string.h>

int main() {
    char str1[100], str2[100];
    printf("Nhap chuoi 1: ");
    fgets(str1, sizeof(str1), stdin);
    printf("Nhap chuoi 2: ");
    fgets(str2, sizeof(str2), stdin);
    int result = strcmp(str1, str2);
    if (result == 0) {
        printf("Hai chuoi giong nhau.\n");
    } else if (result < 0) {
        printf("Chuoi 1 nho hon chuoi 2.\n");
    } else {
        printf("Chuoi 1 lon hon chuoi 2.\n");
    }
    return 0;
}