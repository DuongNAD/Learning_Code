#include <stdio.h>
int main()
{
    int nam, thang;
    printf("Nhap nam ban muon kiem tra = ");
    scanf("%d", &nam);
    printf("Nhap thang ban muon kiem tra = ");
    scanf("%d", &thang);
    int thang31ngay[] = {1, 3, 5, 7, 8, 10, 12};
    int thang30ngay[] = {4, 6, 9, 11};
    int t30 = 0;
    int t31 = 0;
    for (int i = 0; i < 7; i++)
    {
        if (thang == thang31ngay[i])
        {
            t31 = 1;
            break;
        }
    }
    for (int i = 0; i < 4; i++)
    {
        if (thang == thang30ngay[i])
        {
            t30 = 1;
            break;
        }
    }
    if (nam % 400 == 0 || (nam % 4 == 0 && nam % 100 != 0))
    {
        if (t31)
        {
            printf("Thang %d co 31 ngay \n", thang);
        }
        else if (t30)
        {
            printf("Thang %d co 30 ngay \n", thang);
        }
        else if (thang == 2)
        {
            printf("Thang %d co 29 ngay \n", thang);
        }
        else
        {
            printf("Thang khong hop le\n");
        }
    }
    else
    {
        if (t31)
        {
            printf("Thang %d co 31 ngay \n", thang);
        }
        else if (t30)
        {
            printf("Thang %d co 30 ngay \n", thang);
        }
        else if (thang == 2)
        {
            printf("Thang %d co 28 ngay \n", thang);
        }
        else
        {
            printf("Thang khong hop le\n");
        }
    }
    return 0;
}