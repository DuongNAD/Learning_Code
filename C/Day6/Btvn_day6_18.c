#include <stdio.h>
void fibonacii(int n)
{
    int a = 0, b = 1, c;
    if (n < 0)
    {
        printf("Error\n");
        return;
    }
    if (n == 1)
    {
        printf("So fibonacii thu %d la %d\nn", n, a);
        return;
    }
    if (n == 2)
    {
        printf("So fibonacii thu %d la %d", n, b);
        return;
    }
    for (int i = 3; i <= n; i++)
    {
        c = a + b;
        a = b;
        b = c;
    }
    printf("So fibonacii thu %d la %d \n", n, c);
}
int main()
{
    int n;
    printf("Nhap n = ");
    scanf("%d", &n);
    fibonacii(n);
    return 0;
}