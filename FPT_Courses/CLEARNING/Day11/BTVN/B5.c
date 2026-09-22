#include <stdio.h>

int isprime(int n)
{
    if (n <=1)
    {
        return 0;
    }
    for (int i = 2; i * i <= n; i++)
    {
        if (n % i == 0)
        {
            return 0;
        }
    }
    return 1;
}
int main()
{
    FILE *file1, *file2;
    file1 = fopen("Input.txt", "r");
    if (file1 == NULL)
    {
        printf("Error");
        return 1;
    }
    else
    {

        int n, x;
        file2 = fopen("Output.txt", "w");
        fscanf(file1, "%d", &n);
        for (int i = 0; i < n; i++)
        {
            fscanf(file1, "%d", &x);
            if (isprime(x) == 1)
            {
                fprintf(file2, "%d\t", x);
            }
        }
    }
    fclose(file1);
    fclose(file2);
    return 0;
}