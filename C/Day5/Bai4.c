#include <stdio.h>
int main()
{
    int n, sum = 0;
    printf("nhap n = ");
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
    {
        sum = sum +i;
    }
    printf("Tong cac so = %d", sum);
    return 0;
}