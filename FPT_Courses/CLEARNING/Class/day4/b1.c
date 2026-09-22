#include<stdio.h>

int main () {
    int n;
    printf("Nhap n = ");
    scanf("%d",&n);
    if(n<1){
        printf("n pha la so >= 1");
        return 0;
    }
    int count=0;
    for(int i=1;i<=n;i++){
        if(i%2==0){
            count = count +1;
        }
    }
    printf("So so chan trong pham vi 1 den %d = %d",n,count);
    return 0;
}