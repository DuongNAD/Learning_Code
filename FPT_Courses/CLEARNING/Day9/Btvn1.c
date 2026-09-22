#include<stdio.h>

int main () {
    char c[100];
    printf("Nhap chuoi: ");
    fgets(c,sizeof(c),stdin);
    fputs (c,stdout);
    return 0;
}
