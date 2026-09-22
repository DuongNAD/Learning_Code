#include <stdio.h>
int main()
{
    int n;
    printf("Nhap n = ");
    scanf("%d", &n);
    if (n > 30)
    {
        int check = 0;
        for (int i = 2; i <= 5; i += (i == 2 ? 1 : 2))
        {
            if (n % i == 0)
            {
                printf("So %d chia het cho %d\n", n, i);
                check =1;
            }
        }
            if (check == 0)
            {
                printf("So %d khong chia het cho 2,3 hoac 5\n", n);
                check = 1;
            }
    }
    else
    {
        printf("So %d khong lon hon 30 \n", n);
    }
    return 0;
}