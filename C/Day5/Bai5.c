#include <stdio.h>
#include<math.h>
int main()
{
    int n, x; 
    double sum = 0;
    printf("nhap n = ");
    scanf("%d", &n);
    printf("nhap x = ");
    scanf("%d", &x);
    for (int i = 1; i <= n; i++)
    {
        sum = sum +pow(x,i*2);
    }
    printf("Tong cac so = %.2f", sum);
    return 0;
}