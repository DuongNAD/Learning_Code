#include <stdio.h>
int main()
{
    int n;
    printf("Nhap n = ");
    scanf("%d", &n);
    if (n < 2)
    {
        printf("Error\n");
    }
    else
    {
        int true = 1;
        for (int i = 2; i * i <= n; i++)
        {
            if (n % i == 0)
            {
                true = 0;
                break;
            }
        }
        if (true == 1)
        {
            printf("%d la so nguyen to\n",n);
        }
        else
        {
            printf("%d khong phai la so nguyen to\n",n);
        }
    }

    return 0;
}