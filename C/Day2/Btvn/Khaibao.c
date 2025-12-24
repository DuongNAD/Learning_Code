#include <stdio.h>

int main()
{
    float a, b;
    int m,n;
    char c;
    printf("Nhap m va n = ");
    scanf("%d %d",&m,&n);

    printf("Nhap dau c(+,-,*,/): ");
    scanf(" %c", &c);

    printf("Nhap a = ");
    scanf("%f", &a);

    printf("Nhap b = ");
    scanf("%f", &b);

    printf("Gia tri cua a = %.2f\nGia tri cua b = %.2f\n", a, b);
    switch (c)
    {
    case '+':
        printf("a + b = %.2f", a + b);
        break;
    case '-':
        printf("a - b = %.2f", a - b);
        break;
    case '*':
        printf("a * b = %2f", a * b);
        break;
    case '/':
        if (b == 0)
        {
            printf("Khong the chia cho 0");
        }
        else
        {
            printf("a / b = %2f", a / b);
        }
        break;
        default:
        printf("Phep tinh khong hop le");
        break;
    }
    return 0;
}