#include<stdio.h>
int main (){
    int a,b,sum = 0;
    printf("nhap a = ");
    scanf("%d",&a);
    printf("nhap b = ");
    scanf("%d",&b);
    for(int i =a;i<=b;i++){
        sum = sum +i;
    }
    printf("Tong tu a den b = %d",sum);
    return 0;
}