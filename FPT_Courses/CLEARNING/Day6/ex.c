#include <stdio.h>
#include <math.h>
int kiemtrnt(int n)
{
    if (n < 2)
    {
        return -1;
    }
    for (int i = 2; i <= sqrt(n); i++)
    {
        if (n % i == 0)
        {
            return 0;
        }
    }
    return 1;
}
int main()
{
    int n;
    printf("Nhap mot so nguyen: ");
    scanf("%d", &n);
    int nguyento = kiemtrnt(n);
    if (nguyento == -1)
    {
        printf("Error");
    }
    else if (nguyento== 1)
    {
        printf("Day la so nguyen to\n");
    }
    else
    {
        printf("Day khong phai la so nguyen to\n");
    }
    printf("%d",304084888);
    return 0;
}