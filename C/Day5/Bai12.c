#include <stdio.h>
int main()
{
    int n, sum = 0;
    printf("Nhap so n = ");
    scanf("%d", &n);
    int nguyen = n;
    for (; n > 0; n /= 10)
    {
        int a = n % 10;
        sum = sum * 10 + a;
    }
    printf("So dao nguoc cua %d la %d", nguyen, sum);
    return 0;
}