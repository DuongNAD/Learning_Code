#include<stdio.h>

void swap(int *x, int *y){
    printf("%d\t%d\n",*x,*y);    
    int z=*x;
    *x=*y;
    *y=z;
    printf("%d\t%d\n",*x,*y);
}

void nhap_a_b(int *a,int *b){
    printf("Nhap a = ");
    scanf("%d",a);
    printf("Nhap b = ");
    scanf("%d",b);
}
int main (){
    int a,b;
    nhap_a_b(&a,&b);
    swap(&a,&b);
    return 0;
}