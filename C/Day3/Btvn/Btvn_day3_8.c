#include <stdio.h>
int main()
{
    int a, b, c;
    printf("Nhap a = ");
    scanf("%d", &a);
    printf("Nhap b = ");
    scanf("%d", &b);
    printf("Nhap c = ");
    scanf("%d", &c);
    if (a + b > c && b + c > a && a + c > b)
    {
        if (a == b && a == c && b == c)
        {

            printf("Day la tam giac deu: 1\n");
        }
        else if (a * a + b * b == c * c || a * a + c * c == b * b || b * b + c * c == a * a)
        {
            printf("Day la tam giac vuong: 3\n");
        }

        else if (a == b || b == c || a == c)
        {
            printf("Day la tam giac can: 2\n");
        }

        else
        {
            printf("Day la tam giac thuong: 4\n");
        }
    }

    else
    {
        printf("Day khong phai la 3 canh cua tam giac\n");
    }
    return 0;
}