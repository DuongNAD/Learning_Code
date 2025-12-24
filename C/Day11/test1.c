#include<stdio.h>

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

int main () {
    FILE *file;
    printf("Nhap so phan tu trong mang: ");
    scanf("%d",&n);
    arr[n];
    close(file)
    return 0;
}