#include<stdio.h>
int main (){
    int n;
    start:
    printf("Nhap n = ");
    scanf("%d",&n);
    if(n>=30){
        printf("n = %d",n);
    }
    else{
    goto start;
    }
    return 0;
}