#include <stdio.h>
#include <string.h>

int main() {
    char str[100], subStr[100];
    printf("Nhap chuoi: ");
    fgets(str, sizeof(str), stdin);
    printf("Nhap chuoi con: ");
    fgets(subStr, sizeof(subStr), stdin);
    char *ptr = strstr(str, subStr);
    if (ptr != NULL) {
        printf("Chuoi con duoc tim thay tai vi tri: %ld\n", ptr - str);
    } else {
        printf("Khong tim thay chuoi con.\n");
    }
    return 0;
}