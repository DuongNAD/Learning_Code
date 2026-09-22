#include <stdio.h>
#include <math.h>

void isprime(int n)
{
    if (n <= 1)
    {
        return 0;
        for (int i = 2; i * i <= 200; i++)
        {
            if (n % i == 0)
            {
                return 0;
            }
        }
    }
    return 1;
}
void writePrimesToFile(FILE *f, int n)
{
    for (int i = 2; i <= n; i++)
    {
        if (isPrime(i))
        {
            fprintf(f, "%d\t", i);
            printf("%d\t", i);
        }
    }
    printf("\n");
}
int main()
{
    FILE *f;
    f = fopen("prime.txt", "w");
    if (f == NULL)
    {
        printf("Khong the mo file.\n");
        return 1;
    }

    printf("Cac so nguyen to tu 1 den 200:\n");
    writePrimesToFile(f, 200);

    fclose(f);
    printf("Ghi du lieu thanh cong");
    return 0;
}