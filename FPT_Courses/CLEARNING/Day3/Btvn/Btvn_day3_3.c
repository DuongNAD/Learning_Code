#include <stdio.h>
int main()
{
    int n;
    printf("Nhap n = ");
    scanf("%d", &n);
    if (n % 3 == 0 && n % 7 != 0)
    {
        printf("So %d chia het cho ca 3 nhung khong chi het cho 7: 1\n",n);
    }
    else
    {
        printf("So %d không chia hết cho 3 hoặc chia hết cho 7: 0\n",n);
    }
    return 0;
}