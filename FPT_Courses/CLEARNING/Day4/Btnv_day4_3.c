#include<stdio.h>
#include<ctype.h>
int main (){
    char c;
    printf("Nhap so tu 0 den 9: ");
    scanf(" %c",&c);
    if(isdigit(c)){
        printf("Yes");
    }
    else {
        printf("No");
    }
    return 0;
}