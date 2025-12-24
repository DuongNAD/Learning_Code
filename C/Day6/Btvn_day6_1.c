#include <stdio.h>
#include <stdlib.h>
#include <math.h>
long long tong = 0;
int nhap_a_b(int *a, int *b)
{
    printf("Nhap a = ");
    scanf("%d", a);
    printf("Nhap b = ");
    scanf("%d", b);
}
int nhap_n(int *n)
{
    printf("Nhap n = ");
    do
    {
        scanf("%d", n);
        if (*n <= 0)
        {
            printf("%d khong hop le\nMoi nhap lai n(n>0) = ", *n);
        }
    } while (*n <= 0);
}
int nhap_x(int *x)
{
    printf("Nhap x = ");
    do
    {
        scanf("%d", x);
        if (*x <= 0)
        {
            printf("%d khong hop le \nMoi nhap lai x(x>0) = ", *x);
        }
    } while (*x <= 0);
}

int tong_a_b(int a, int b)
{
    nhap_a_b(&a, &b);
    long long tong = 0;
    for (int i = a; i <= b; i++)
    {
        tong = tong + i;
    }
    return tong;
}

int tongchan_a_b(int a, int b)
{
    nhap_a_b(&a, &b);
    long long tong = 0;
    for (int i = a; i <= b; i++)
    {
        if (i % 2 == 0)
        {
            tong = tong + i;
        }
    }
    return tong;
}

int Stong(int n)
{
    nhap_n(&n);
    long long tong = 0;
    for (int i = 1; i <= n; i++)
    {
        tong = tong + i;
    }
    return tong;
}

void in()
{
    printf("10 so dau tien la ");
    for (int i = 0; i < 10; i++)
    {
        printf("%d\t", i);
    }
    printf("\n");
}

int Smuchan(int x, int n)
{
    nhap_x(&x);
    nhap_n(&n);
    long long tong = 0;
    for (int i = 1; i <= n; i++)
    {
        tong = tong + pow(x, 2 * i);
    }
    return tong;
}

long long Smule(int x, int n)
{
    nhap_x(&x);
    nhap_n(&n);
    long long tong = 0;
    for (int i = 1; i <= n; i++)
    {
        tong = tong + pow(x, 2 * i - 1);
    }
    return tong;
}

void uocle(int n)
{
    nhap_n(&n);
    for (int i = 1; i <= n; i++)
    {
        if (n % i == 0 && i % 2 == 1)
        {
            printf("%d\t", i);
        }
    }
}

int giaithua(int n)
{
    nhap_n(&n);
    long long tong = 1;
    if (n < 0)
    {
        printf("Error\n");
        return -1;
    }
    for (int i = 1; i <= n; i++)
    {
        tong = tong * i;
    }
    printf("%d! = %lld\n", n, tong);
}

void bangcuuchuong()
{
    for (int i = 1; i <= 10; i++)
    {
        for (int j = 1; j <= 10; j++)
        {
            printf("%d * %d = %d\t", i, j, i * j);
        }
        printf("\n");
    }
}

int nhap28(int n)
{
    while (1)
    {
        nhap_n(&n);
        if (n == 28)
        {
            break;
        }
        else
        {
            printf("Moi nhap so 28 de thoat chuong trinh ");
        }
    }
    printf("Chuong trinh da ket thuc\n");
    return 0;
}

int ktnguyento(int n)
{
    nhap_n(&n);
    int dung = 1;
    if (n < 2)
    {
        printf("Error: so nguyen to phai lon hon 1\n");
        return 0;
    }
    else
    {
        for (int i = 2; i * i <= n; i++)
        {
            if (n % i == 0)
            {
                dung = 0;
                break;
            }
        }
    }
    if (dung == 1)
    {
        printf("%d la so nguyen to\n", n);
    }
    else
    {
        printf("%d khong phai la so nguyen to\n", n);
    }
    return 0;
}

int sodaonguoc(int n)
{
    nhap_n(&n);
    int tong = 0;
    for (; n > 0; n /= 10)
    {
        tong = tong * 10 + (n % 10);
    }
    printf("%d\n", tong);
    return tong;
}

void ktsodaonguoc(int n)
{
    nhap_n(&n);
    int nt = n;
    int tong = 0;
    for (; n > 0; n /= 10)
    {
        tong = tong * 10 + (n % 10);
    }
    if (nt == tong)
    {
        printf("%d la so dao nguoc \n", nt);
    }
    else
    {
        printf("%d khong phai so dao nguoc \n", nt);
    }
}

void sodep(int n)
{
    nhap_n(&n);
    int tong = 0;
    int nt = n;
    for (; n > 0; n /= 10)
    {
        tong = tong + (n % 10);
    }
    if (tong == 9)
    {
        printf("%d la so dep", nt);
    }
    else
    {
        printf("%d khong phai so dep", nt);
    }
}

int main()
{
    int luachon;
    int a, b, n, x;
    char tieptuc;
    do
    {
        printf("\n");
        printf("==========================MENU========================\n");
        printf("1. In ra man hinh 10 so tu nhien dau tien\n");
        printf("2. Nhap vao doan [a,b]. In ra man hinh tong cac so tu a den b\n");
        printf("3. Nhap vao doan [a,b]. In ra tong cac so chan tu a den b\n");
        printf("4. Tinh S(n) = 1 + 2 + 3 + 4 + ... + n =\n");
        printf("5. Tinh S(n) = x^2 + x^4 + ... + x^2n = \n");
        printf("6. Tinh S(n) = x + x^3 +x^5 + ... + x^(2n-1) = \n");
        printf("7. Liet ke tat ca cac uoc le cua so nguyen n\n");
        printf("8. Tinh N giai thua\n");
        printf("9. In ra man hinh bang cuu chuong\n");
        printf("10. Nhap tu ban phim cho toi khi nhap so 28 thi dung\n");
        printf("11. Kiem tra xem n co phai so nguyen to khong\n");
        printf("12. Nhap vao so n. In ra so dao nguoc\n");
        printf("13. Nhap vao so n. Xac dinh n co phai so dao nguoc khong\n");
        printf("14. Nhap vao so n. Kiem tra xem n co phai so dep khong\n");
        printf("15. Thoat chuong trinh\n");
        printf("=====================================================\n");
        printf("\nChon tu (1 - 15): ");
        scanf("%d", &luachon);
        printf("\n");
        switch (luachon)
        {
        case 1:
            in();
            break;
        case 2:
            printf("Tong cac so tu a den b = %lld\n", tong_a_b(a, b));
            break;
        case 3:
            printf("Tong cac so chan tu a den b = %lld\n ", tongchan_a_b(a, b));
            break;
        case 4:
            printf("S(n) = %lld\n", Stong(n));
            break;
        case 5:
            printf("S(n) = %lld\n", Smuchan(x, n));
            break;
        case 6:
            printf("S(n) = %lld\n", Smule(x, n));
            break;
        case 7:
            printf("Cac uoc le cua n la: \n");
            uocle(n);
            break;
        case 8:
            giaithua(n);
            break;
        case 9:
            printf("Bang cuu chuong \n");
            bangcuuchuong();
            break;
        case 10:
            nhap28(n);
            break;
        case 11:
            ktnguyento(n);
            break;
        case 12:
            sodaonguoc(n);
            break;
        case 13:
            ktsodaonguoc(n);
            break;
        case 14:
            sodep(n);
            break;
        case 15:
            printf("Chuong trinh da ket thuc. \n");
            return 0;
        default:
            printf("Lua chon khong hop le\nMoi chon lai\n");
            break;
        }
        printf("\nBan co muon thuc hien tiep (y/n)? ");
        scanf(" %c", &tieptuc);
    } while (tieptuc == 'y' || tieptuc == 'Y');
    printf("Chuong trinh da ket thuc. \n");
    return 0;
}