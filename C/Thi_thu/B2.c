// Bài 2: Kiểm tra số nguyên tố (10 điểm)
// Viết chương trình nhập vào một số nguyên n, kiểm tra xem n có phải số nguyên tố không.
#include <stdio.h>
#include <math.h>

int main()
{
    int n;
    printf("Nhap so muon kiem tra: ");
    if (scanf("%d", &n) != 1)
    {
        printf("Error\n");
        return 0;
    }

    for (int i = 2; i <= sqrt(n); i++)
    {
        if (n % i == 0)
        {
            printf("%d khong phai la so nguyen to\n", n);
            return 0;
        }
    }
    printf("%d la so nguyen to\n", n);
    return 0;
}