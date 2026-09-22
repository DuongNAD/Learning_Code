#include<stdio.h>
 void nhap_n(int *n){
    printf("Nhap n = ");
    scanf("%d",n);
 }
 int main (){
    int n;
    nhap_n(&n);
    printf("%d",n);
    return 0;
 }