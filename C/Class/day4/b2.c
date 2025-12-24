#include <stdio.h>

int main()
{
    int num;
    long long sum = 0;
    int count = 0;
    printf("Nhap vao cac so nguyen duong (nhap 0 de ket thuc):\n");

    while (1)
    {
        scanf("%d", &num);

        if (num == 0)
        {
            break;
        }

        if (num > 0)
        {
            sum += num;
            count++;
        }
    }

    if (count > 0)
    {
        double average = (double)sum / count;

        printf("Gia tri trung binh cong la: %g\n", average);
    }
    else
    {
        printf("Ban chua nhap so nguyen duong nao de tinh trung binh.\n");
    }
    
    return 0;
}