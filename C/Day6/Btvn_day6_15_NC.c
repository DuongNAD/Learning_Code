#include <stdio.h>
int main()
{
    int n;
    int tong = 0;
    printf("Nhap n = ");
    scanf("%d", &n);
    if (n <= 0)
    {
        printf("Error\n");
        return 0;
    }
    for (int i = 1; i <= n; i++)
    {
        if (n % i == 0)
        {
            tong = tong + i;
        }
    }
    printf("Tong cac uoc cua %d = %d", n, tong);
}