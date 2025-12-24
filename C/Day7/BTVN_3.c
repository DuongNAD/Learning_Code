#include <stdio.h>
void nhap_a(int *a)
{
    printf("Nhap a = ");
    scanf("%d", a);
}
void increment(int *n)
{

    (*n)++;
    printf("%d", *n);
}

int main()
{
    int a;
    nhap_a(&a);
    increment(&a);
    return 0;
}