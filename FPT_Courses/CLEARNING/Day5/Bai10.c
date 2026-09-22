#include <stdio.h>
#include <math.h>
int main()
{
    int n;
    printf("Nhap n = ");
    scanf("%d", &n);
    for (; n != 28;)
    {
        printf("Nhap n = 28 de thoat: ");
        scanf("%d", &n);
    }
    return 0;
}