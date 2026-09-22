#include <stdio.h>
int main()
{
    float a, b;
    char c;
    printf("Nhap a = ");
    scanf("%f", &a);
    printf("\nNhap b = ");
    scanf("%f", &b);
    printf("\nNhap dau (+,-,*,/): ");
    scanf(" %c", &c);
    printf ("%.2f %c %.2f = ",a,c,b);
    switch (c)
    {
    case '+':
        printf("%.2f\n", a + b);
        break;
    case '-':
        printf("%.2f\n", a - b);
        break;
    case '*':
        printf("%.2f\n", a * b);
        break;
    case '/':
        if (b == 0)
        {
            printf("\nLoi do khong the chia cho 0 ");
        }
        else
        {
            printf("%.2f\n", a / b);
        }
        break;
    default:
        printf("\nToan tu khong hop le");
        break;
    }
    return 0;
}