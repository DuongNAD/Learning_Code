#include <stdio.h>
#include <math.h>
int main()
{
    float r, cv, s;
    const float pi = 3.14159;
    printf("Nhap ban kinh r (r>0) = ");
    scanf("%f", &r);
    if (r <= 0)
    {
        printf("Ban kinh r phai lon hon 0\n ");
    }
    else
    {
        cv = 2 * pi * r;
        s = pi * r * r;
        printf("Chu vi hinh tron = %.2f\nDien tich hinh tron = %.2f\n", cv, s);
    }
    return 0;
}