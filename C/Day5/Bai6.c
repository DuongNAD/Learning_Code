#include <stdio.h>
#include<math.h>
int main()
{
    int n, x;
    double sum = 1;
    printf("Nhap n = ");
    scanf("%d",&n);
    printf("Nhap x = ");
    scanf("%d",&x);
    for (int i = 1; i <= n; i++)
    {
        if (i % 3 == 0)
        {
            sum = sum * pow(x, 2 * i - 1);
        }
    }
    printf("Tong cac so = %.0f", sum);
    return 0;
}