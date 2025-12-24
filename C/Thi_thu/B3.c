// Bài 3: Tính tổng số chẵn từ 1 đến n (10 điểm)
// Viết chương trình tính tổng các số chẵn từ 1 đến n.

#include <stdio.h>

int main()
{
    int n;
    printf("Nhap n = ");
    if (scanf("%d", &n) != 1 || n < 2)
    {
        printf("Error");
        return 0;
    }
    int sum = 0;
    for (int i = 0; i <= n; i++)
    {
        if (i % 2 == 0)
        {
            sum = sum + i;
        }
    }
    printf("Tong cac so chan tu 1 den %d = %d", n, sum);
    return 0;
}