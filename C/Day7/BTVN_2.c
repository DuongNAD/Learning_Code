#include <stdio.h>
void nhap_a_b(int *a, int *b)
{
    printf("Nhap a = ");
    scanf("%d", a);
    printf("Nhap b = ");
    scanf("%d", b);
}

void calculateSum(int *x, int *y)
{
    int z = *x + *y;
    printf("Tong = %d\n", z);
}

int main()
{
    int a, b, z;
    nhap_a_b(&a, &b);
    calculateSum(&a, &b);
    return 0;
}