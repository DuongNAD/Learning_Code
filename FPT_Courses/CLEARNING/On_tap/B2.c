#include <stdio.h>

void swap(int *a, int *b)
{
    printf("Nhap a = ");
    scanf("%d", a);
    printf("Nhap b = ");
    scanf("%d", b);

    printf("Truoc khi doi: \n");
    printf("a = %d\t", *a);
    printf("b = %d\t", *b);
    printf("\n");
    
    int c = *a;
    *a = *b;
    *b = c;

    printf("Sau khi doi: \n");
    printf("a = %d\t", *a);
    printf("b = %d\t", *b);
}

int main()
{
    int a, b;
    swap(&a, &b);
    return 0;
}