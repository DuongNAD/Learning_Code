#include <stdio.h>
int main()
{
    int n, sum = 0;
    printf("Nhap n = ");
    scanf("%d", &n);
    int thuc = n;
    for (; n > 0; n /= 10)
    {
        int a = n % 10;
        sum = sum + a;
    }
    if (sum == 9)
    {
        printf("%d la so dep", thuc);
    }
    else
    {
        printf("%d khong phai la so dep", thuc);
    }
    return 0;
}