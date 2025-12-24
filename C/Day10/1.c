#include <stdio.h>

typedef struct Phan_so
{
    int tu;
    int mau;
} PS;

void nhap(PS *ps)
{
    printf("Tu = ");
    scanf("%d", &ps->tu);
    do
    {
        printf("Mau = ");
        scanf("%d", &ps->mau);
        if (ps->mau == 0)
        {
            printf("Mau so phai khac 0\n");
            printf("Moi nhap lai");
        }

    } while (ps->mau == 0);
}

void xuat(PS ps)
{
    printf("%d/%d", ps.tu, ps.mau);
}

void nhap_PS(PS ps[])
{
    for (int i = 0; i < 2; i++)
    {
        printf("Nhap phan so thu %d: \n", i + 1);
        nhap(&ps[i]);
    }
}

void xuat_PS(PS ps[])
{
    for (int i = 0; i < 2; i++)
    {
        printf("Phan so thu %d: ", i + 1);
        xuat(ps[i]);
        printf("\n");
    }
}

int ucln(int a, int b)
{
    if (a == 0 || b == 0)
    {
        return a + b;
    }
    int ucln;
    int max = a < b ? a : b;
    for (int i = max; i >= 1; i--)
    {
        if (a % i == 0 && b % i == 0)
        {
            ucln = i;
            break;
        }
    }
    return ucln;
}

void calculator_addition(PS ps[])
{

    int tu1 = ps[0].tu;
    int mau1 = ps[0].mau;
    int tu2 = ps[1].tu;
    int mau2 = ps[1].mau;
    int sum_tu, sum_mau;

    if (mau1 == mau2)
    {
        sum_tu = tu1 + tu2;
        sum_mau = mau1;
        int ucln_valua = ucln(sum_tu, sum_mau);
        printf("%d/%d + %d/%d = %d/%d", tu1, mau1, tu2, mau2, sum_tu, mau2);
        printf("\n");
        if (sum_tu % ucln_valua == 0 && sum_mau % ucln_valua == 0)
        {
            printf("Rut gon phan so: ");
            sum_tu /= ucln_valua;
            sum_mau /= ucln_valua;
            printf("%d/%d", sum_tu, sum_mau);
        }
    }
    else
    {
        sum_mau = mau1 * mau2;
        sum_tu = tu1 * mau2 + tu2 * mau1;
        int ucln_valua = ucln(sum_tu, sum_mau);
        printf("%d/%d + %d/%d = %d/%d", tu1, mau1, tu2, mau2, sum_tu, sum_mau);
        printf("\n");
        if (sum_tu % ucln_valua == 0 && sum_mau % ucln_valua == 0)
        {
            printf("Rut gon phan so: ");
            sum_tu /= ucln_valua;
            sum_mau /= ucln_valua;
            printf("%d/%d", sum_tu, sum_mau);
        }
    }
}

void calculator_subtraction(PS ps[])
{

    int tu1 = ps[0].tu;
    int mau1 = ps[0].mau;
    int tu2 = ps[1].tu;
    int mau2 = ps[1].mau;
    int sum_tu, sum_mau;

    if (mau1 == mau2)
    {
        sum_tu = tu1 - tu2;
        sum_mau = mau1;
        int ucln_valua = ucln(sum_tu, sum_mau);
        printf("%d/%d - %d/%d = %d/%d", tu1, mau1, tu2, mau2, sum_tu, mau2);
        printf("\n");
        if (sum_tu % ucln_valua == 0 && sum_mau % ucln_valua == 0)
        {
            printf("Rut gon phan so: ");
            sum_tu /= ucln_valua;
            sum_mau /= ucln_valua;
            printf("%d/%d", sum_tu, sum_mau);
        }
    }
    else
    {
        sum_mau = mau1 * mau2;
        sum_tu = tu1 * mau2 - tu2 * mau1;
        int ucln_valua = ucln(sum_tu, sum_mau);
        printf("%d/%d - %d/%d = %d/%d", tu1, mau1, tu2, mau2, sum_tu, sum_mau);
        printf("\n");
        if (sum_tu % ucln_valua == 0 && sum_mau % ucln_valua == 0)
        {
            printf("Rut gon phan so: ");
            sum_tu /= ucln_valua;
            sum_mau /= ucln_valua;
            printf("%d/%d", sum_tu, sum_mau);
        }
    }
}

void calculator_multiplication(PS ps[])
{

    int tu1 = ps[0].tu;
    int mau1 = ps[0].mau;
    int tu2 = ps[1].tu;
    int mau2 = ps[1].mau;
    int sum_tu, sum_mau;

    sum_tu = tu1 * tu2;
    sum_mau = mau1 * mau2;
    int ucln_valua = ucln(sum_tu, sum_mau);
    printf("%d/%d * %d/%d = %d/%d", tu1, mau1, tu2, mau2, sum_tu, sum_mau);
    printf("\n");
    if (sum_tu % ucln_valua == 0 && sum_mau % ucln_valua == 0)
    {
        printf("Rut gon phan so: ");
        sum_tu /= ucln_valua;
        sum_mau /= ucln_valua;
        printf("%d/%d", sum_tu, sum_mau);
    }
}

void calculator_division(PS ps[])
{

    int tu1 = ps[0].tu;
    int mau1 = ps[0].mau;
    int tu2 = ps[1].tu;
    int mau2 = ps[1].mau;
    int sum_tu, sum_mau;

    sum_tu = tu1 * mau2;
    sum_mau = mau1 * tu2;
    int ucln_valua = ucln(sum_tu, sum_mau);
    printf("%d/%d / %d/%d = %d/%d", tu1, mau1, tu2, mau2, sum_tu, sum_mau);
    printf("\n");
    if (sum_tu % ucln_valua == 0 && sum_mau % ucln_valua == 0)
    {
        printf("Rut gon phan so: ");
        sum_tu /= ucln_valua;
        sum_mau /= ucln_valua;
        printf("%d/%d", sum_tu, sum_mau);
    }
}

int main()
{
    PS ps[100];
    nhap_PS(ps);
    xuat_PS(ps);
    char c;
    printf("Nhap dau: ");
    getchar();
    scanf("%c", &c);

    switch (c)
    {
    case '+':
        calculator_addition(ps);
        break;
    case '-':
        calculator_subtraction(ps);
        break;
    case '*':
        calculator_multiplication(ps);
        break;
    case '/':
        calculator_division(ps);
        break;
    default:
        printf("Toan tu khong hop le");
        break;
    }
    return 0;
}
