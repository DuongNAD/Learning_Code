#include <stdio.h>

int main(){
    int n, b;
    long tich =1 ;
    int i =1;
    printf("nhap n = ");
    scanf("%d", n);
    if (n<1)
    {
        printf("n phai la 1 so >=1\n");
    }
    
    while (1)
    {
        if (n ='\n')
        {
            break;
        }
        if (i<=n)
        {

           tich = i* tich;
           i++;
        }
        
        
    }
    printf("%d! = %d",i,tich);
    return 0;   
}
