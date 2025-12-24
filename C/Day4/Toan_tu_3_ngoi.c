#include <stdio.h>
int main()
{
    int n;
    printf("Nhap n = ");
    scanf("%d", &n);
    (n >= 0&&(n % 2 == 0 || n % 3 == 0 || n % 5 == 0)) ? printf("1")
                                                                     : printf("0");
    return 0;
}