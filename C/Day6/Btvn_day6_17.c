#include <stdio.h>
int main()
{
    int n, tong = 0;
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
            if (tong == n)
            {
                printf("%d la so hoan hao\n", n);
                return 0;
            }
        }
    }
    printf("%d khong phai la so hoan hao\n",n);
    return 0;
}