#include<stdio.h>
int main (){
    int n;
    printf("Nhap n = ");
    scanf("%d",&n);
    for(int i =0;i*i<=n;i++){
        if(i*i ==n){
            printf("%d la so chinh phuong\n",n);
            return 0;
        }
    }
    printf("%d khong phai la so chinh phuong\n",n);
    return 0;
}