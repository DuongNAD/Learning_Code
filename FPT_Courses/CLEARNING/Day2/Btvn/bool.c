#include<stdio.h>
#include<stdbool.h>
int main (){
    int a,b;
    char c;
    bool x = true;
    bool y = false;
    
    printf("Nhap a = ");
    scanf("%d",&a);
    printf ("Nhap b = ");
    scanf("%d",&b);
    if (a==b){
        printf("%s",x ? "True":"False");
    }
    else{
        printf("%s",y ? "True":"False");
    }
    return 0;
}