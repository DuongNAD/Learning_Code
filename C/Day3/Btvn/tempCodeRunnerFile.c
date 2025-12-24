#include <stdio.h>
int main()
{
    int n;
    printf("Nhap n = ");
    scanf("%d", &n);
    if (n>30){
        if(n%2==0){
            printf("So %d la so chia het cho 2\n",n);
        }
        if(n%3==0){
            printf("So %d la so chia het cho 3\n",n);
        }
        if(n%5==0){
            printf("So %d la so chia het cho 5\n",n);
        }
        else {
            printf ("So %d khong chia het cho 2,3 hoac 5\n",n);
        }
    }
    else{
        printf ("So %d khong lon hon 30 \n",n);
    }
    return 0;
}