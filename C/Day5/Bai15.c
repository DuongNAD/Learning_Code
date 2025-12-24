#include <stdio.h>
int main()
{
    int a, b;
    printf("Nhap chieu dai a = ");
    scanf("%d", &a);
    printf("Nhap chieu rong b = ");
    scanf("%d", &b);
    for (int i = 1; i <= a; i++)
    {
        for (int j = 1; j <= b; j++)
        {
            if (i == 1 || i == a || j == 1 || j == b)
            {
                printf("* ");
            }
            else
            {
                printf("  ");
            }
        }
        printf("\n");
    }
    return 0;
}