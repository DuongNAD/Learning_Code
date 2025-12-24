#include <stdio.h>
int main()
{
    int n;
    printf("Nhap n = ");
    scanf("%d", &n);
    printf("Cac uoc le cua %d la: ",n);
    for (int i = 1; i <= n; i++)
    {
        if (n % i == 0 && i % 2 == 1)
        {
            printf("%d ", i);
        }
    }
    return 0;
}