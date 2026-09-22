#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

void Input(int c[], int *n)
{
    for (int i = 0; i < *n; i++)
    {

        printf("Gia tri %d: ", i + 1);
        scanf("%d", &c[i]);
    }

    printf("\n");
}

void Output(int c[], int n)
{
    printf("Gia tri da nhap: \n");
    for (int i = 0; i < n; i++)
    {
        printf("Gia tri %d: %d\n", i + 1, c[i]);
    }
    printf("\n");
}

void findMax(int c[], int n)
{
    int Max = c[0];
    for (int i = 1; i < n; i++)
    {

        if (Max < c[i])
        {
            Max = c[i];
        }
    }
    printf("Max = %d", Max);
}

void findMin(int c[], int n)
{
    int Min = c[0];
    for (int i = 1; i < n; i++)
    {
        if (c[i] < Min)
        {
            Min = c[i];
        }
    }
    printf("Min = %d", Min);
}

void So_thuan_nghich(int c[], int n)
{
    int count = 0;
    printf("Cac so thuan nghich la: \n");
    for (int i = 0; i < n; i++)
    {
        if (c[i] < 0)
        {
            continue;
        }

        int num = c[i];
        int div = 1;

        while (num / div >= 10)
        {
            div *= 10;
        }

        int is_palindrome = 1;
        while (num != 0)
        {
            int right = num / div;
            int left = num % 10;

            if (left != right)
            {
                is_palindrome = 0;
                break;
            }

            num = (num % div) / 10;
            div /= 100;
        }

        if (is_palindrome == 1)
        {
            printf("%d\t", c[i]);
            count++;
        }
    }
    printf("So thuan nghich trong mang la: %d\n", count);
}

void prime_number(int c[], int n)
{

    int count = 0;

    printf("Cac so nguyen to la: \n");
    for (int i = 0; i < n; i++)
    {
        if (c[i] < 2)
        {
            continue;
        }
        int Check_prime = 1;
        for (int j = 2; j * j <= c[i]; j++)
        {
            if (c[i] % j == 0)
            {

                Check_prime = 0;
                break;
            }
        }
        if (Check_prime == 1)
        {
            printf("%d\t", c[i]);
            count++;
        }
    }
    printf("So nguyen to trong mang la: %d\n", count);
}

void ascending(int c[], int n)
{
    int swap;
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (c[i] > c[j])
            {
                swap = c[i];
                c[i] = c[j];
                c[j] = swap;
            }
        }
    }
    printf("Mang theo thu tu tang dan la: \n");
    for (int i = 0; i < n; i++)
    {
        printf("%d\t", c[i]);
    }
}

void decreasing(int c[], int n)
{
    int swap;
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (c[i] < c[j])
            {
                swap = c[i];
                c[i] = c[j];
                c[j] = swap;
            }
        }
    }
    printf("Mang theo thu tu giam dan la: \n");
    for (int i = 0; i < n; i++)
    {
        printf("%d\t", c[i]);
    }
}

void frequency_V(int c[], int n)
{
    int check;
    printf("Nhap so muon kiem tra: ");
    scanf("%d", &check);
    int count = 0;
    for (int i = 0; i < n; i++)
    {
        if (c[i] == check)
        {
            count++;
        }
    }
    printf("So %d xuat hien %d lan", check, count);
}

void frequency(int c[], int n)
{
    bool visited[n];
    for (int i = 0; i < n; i++)
        visited[i] = false;

    for (int i = 0; i < n; i++)
    {
        if (visited[i])
            continue;

        int count = 1;
        for (int j = i + 1; j < n; j++)
        {
            if (c[i] == c[j])
            {
                count++;
                visited[j] = true;
            }
        }

        printf("So %d xuat hien %d lan\n", c[i], count);
    }
}

void Add(int c[], int *n)
{
    int add_V;
    int visit;
    printf("Nhap gia tri muon them: ");
    scanf("%d", &add_V);
    printf("Nhap vi tri muon them: ");
    scanf("%d", &visit);
    if (visit < 0 || visit > *n)
    {
        printf("Vi tri khong hop le\n");
        return;
    }
    for (int i = *n; i > visit; i--)
    {
        c[i] = c[i - 1];
    }
    c[visit] = add_V;
    (*n)++;

    printf("Chuoi sau khi nhap:\n");
    for (int i = 0; i < *n; i++)
    {
        printf("%d\t", c[i]);
    }
}

void clear(int c[], int *n)
{
    int visit;
    printf("Nhap vi tri muon xoa: ");
    scanf("%d", &visit);

    if (visit < 0 || visit > *n)
    {
        printf("Vi tri khong hop le\n");
        return;
    }

    for (int i = visit; i < *n; i++)
    {
        c[i] = c[i + 1];
    }
    (*n)--;
    printf("Chuoi sau khi xoa:\n");
    for (int i = 0; i < *n; i++)
    {
        printf("%d\t", c[i]);
    }
}

void clear_all(int c[], int *n)
{
    int clear;
    int i = 0;
    printf("Nhap gia tri muon xoa: ");
    scanf("%d", &clear);

    while (i < *n)
    {
        if (c[i] == clear)
        {
            for (int j =i; j < *n - 1; j++)
            {

                c[j] = c[j + 1];
            }
            (*n)--;
        }
        else
        {
            i++;
        }
    }

    printf("Chuoi sau khi xoa:\n");
    for (int i = 0; i < *n; i++)
    {
        printf("%d\t", c[i]);
    }
}

void reverse(int c[], int *n)
{
    for (int i = 0; i < *n / 2; i++)
    {
        int temp = c[i];
        c[i] = c[*n - i - 1];
        c[*n - i - 1] = temp;
    }

    printf("Chuoi sau khi dao nguoc: \n");
    for (int i = 0; i < *n; i++)
    {
        printf("%d\t", c[i]);
    }
    printf("\n");
}

void check_ascending(int c[], int *n)
{

    for (int i = 0; i < *n - 1; i++)
    {
        if (c[i] > c[i + 1])
        {
            printf("No");
            return;
        }
    }
    printf("Yes");
}

int main()
{
    int n, chose;
    char tieptuc;
    printf("Nhap so gia tri muon nhap: ");
    scanf("%d", &n);
    int *c = (int *)malloc(n * sizeof(int));

    c = (int *)malloc(n * sizeof(int));
    if (c == NULL)
    {
        printf("Error\n");
        return 1;
    }
    Input(c, &n);

    Output(c, n);
    do
    {
        printf("============================MENU==========================\n");
        printf("1. Tim max\n");
        printf("2. Tim min\n");
        printf("3. So thuan nghich\n");
        printf("4. So nguyen to\n");
        printf("5. Sap xep theo thu tu tang dan\n");
        printf("6. Sap xep theo thu tu giam dan\n");
        printf("7. Dem so lan xuat hien cua gia tri V\n");
        printf("8. Tan so xuat hien cua cac gia tri trong mang\n");
        printf("9. Them phan tu gia tri V tai vi tri k\n");
        printf("10. Xoa phan tu tai vi tri k\n");
        printf("11. Xoa tat ca phan tu co gia tri k\n");
        printf("12. Dao nguoc mang\n");
        printf("13. Kiem tra xem mang co tang dan khong\n");
        printf("14. Thoat chuong trinh\n");
        printf("===========================================================\n");
        printf("\n");
        printf("Chon tu 1 - 14: ");
        scanf("%d", &chose);
        getchar();
        printf("\n");
        switch (chose)
        {
        case 1:
            findMax(c, n);
            break;
        case 2:
            findMin(c, n);
            break;
        case 3:
            So_thuan_nghich(c, n);
            break;
        case 4:
            prime_number(c, n);
            break;
        case 5:
            ascending(c, n);
            break;
        case 6:
            decreasing(c, n);
            break;
        case 7:
            frequency_V(c, n);
            break;
        case 8:
            frequency(c, n);
            break;
        case 9:
            Add(c, &n);
            break;
        case 10:
            clear(c, &n);
            break;
        case 11:
            clear_all(c, &n);
            break;
        case 12:
            reverse(c, &n);
            break;
        case 13:
            check_ascending(c, &n);
            break;
        case 14:
            printf("Chuong trinh da ket thuc \n");
            return 0;
        default:
            printf("Error\n");
            break;
        }
        printf("\n");
        printf("Ban co muon tiep tuc chuong trinh khong (y/n): ");
        scanf("%c", &tieptuc);
        while ((getchar()) != '\n')
            ;
    } while (tieptuc == 'y' || tieptuc == 'Y');
    free(c);
    return 0;
}
