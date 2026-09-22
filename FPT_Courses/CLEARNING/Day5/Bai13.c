#include<stdio.h>
int main (){
    int n,sum =0;
    printf("Nhap so n = ");
    scanf("%d",&n);
    int thuc =n;
    for(;n>0;n /=10){
        int a = n%10;
        sum = sum*10 +a;
    }
    if(sum == thuc){
        printf("%d la so dao nguoc",thuc);
    }
    else{
        printf("%d khong phai so dao nguoc",thuc);
    }
    return 0;
}