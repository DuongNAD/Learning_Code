#include <stdio.h>
#include <math.h>
int main()
{
    float a, b, c, p, cv, s;
    printf("Nhap a = ");
    scanf("%f", &a);
    printf("Nhap b = ");
    scanf("%f", &b);
    printf("Nhap c = ");
    scanf("%f", &c);
    if (a + b > c && a + c > b && b + c > a)
    {
        cv = a + b + c;
        p = cv / 2;
        s = sqrt(p * (p - a) * (p - b) * (p - c));
        printf("Chu vi tam giac = %.2f\nDien tich tam giac = %.2f\n", cv, s);
    }
    else
        printf("Day khong phai la tam giac\n");
    return 0;
}