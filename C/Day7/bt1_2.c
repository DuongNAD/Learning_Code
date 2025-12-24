#include <stdio.h>

void swap_pointer(int *x, int *y)
{
    printf("%d %d\n", *x, *y);
    int z = *x;
    *x = *y;
    *y = z;
printf("%d %d\n", *x, *y);
}

void tru(int *n)
{
    printf("Nhap n = ");
    scanf("%d", n);
    *n = *n + 1;
}

int main()
{
    int a = 10, b = 20, n;
    swap_pointer(&a, &b);
    tru(&n);    
    printf("%d",n);
    return 0;
}