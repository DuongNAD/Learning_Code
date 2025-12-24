#include <stdio.h>
#include<math.h>
int main()
{
    float a, b;
    printf("Nhap a = ");
    scanf("%f", &a);
    printf("Nhap b = ");
    scanf("%f", &b);
    printf("a + b = %.2f\n", a + b);
    printf("a - b = %.2f\n", a - b);
    printf("a * b = %.2f\n", a * b);
    if (b == 0){
        printf("Khong hop le");
    }
    else
    {
        printf("a / b = %.0f\n", a / b);
        printf("a / b = %.2f\n", a / b);
        printf("a %% b = %.0f\n",fmod(a,b));
    }
    return 0;
}