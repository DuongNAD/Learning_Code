#include <stdio.h>
int main()
{
    int n;
    printf("Nhap n = ");
    scanf("%d", &n);
    if (n % 3 == 0 && n % 5 == 0)
    {
        printf("n chia het cho ca 3 va 5: 1\n");
    }
    else
    {
        printf("n khong chia het cho ca 3 va 5: 0\n");
    }
    return 0;
}