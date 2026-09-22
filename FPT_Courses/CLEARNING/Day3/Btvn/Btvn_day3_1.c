#include <stdio.h>
int main()
{
    int n;
    printf("Nhap n = ");
    scanf("%d", &n);
    if (n % 2 == 0)
    {
        printf("n la so chan\n");
    }
    else
    {
        printf("n la so le\n");
    }
    return 0;
}