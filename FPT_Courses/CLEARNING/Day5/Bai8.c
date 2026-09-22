#include <stdio.h>
int main()
{
    int n;
    long long sum = 1;
    printf("nhap n = ");
    scanf("%d", &n);
    if (n < 0)
    {
        printf("Error \n");
        return 0;
    }
    else if(n==0){
        printf("giai thua cua 0 = 1\n");
    }
    else
    {
        for (int i = 1; i <= n; i++)
        {
            sum = sum * i;
        }
    }
    printf("Tong n giai thua = %lld\n", sum);
    return 0;
}