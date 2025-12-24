#include<stdio.h>
#include<ctype.h>
int main (){
    char c;
    printf("Nhap mot ki tu: ");
    scanf("%c",&c);
    if (islower(c)||isupper(c)){
        printf("Yes");
    }
    else{
        printf("No");
    }
    return 0;
}