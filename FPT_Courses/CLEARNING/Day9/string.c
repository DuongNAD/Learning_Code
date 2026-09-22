#include<stdio.h>
#include<string.h>
int main () {
    char c[10];
    fgets(c,sizeof(c),stdin);
    fputs(c,stdout);
    return 0;
}