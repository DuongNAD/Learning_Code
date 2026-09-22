#include <stdio.h>

void isPrime(FILE *file)
{
    int count = 0;
    for (int i = 2; i <= 200; i++)
    {

        int sont = 1;
        for (int j = 2; j * j <= i; j++)
        {
            if (i % j == 0)
            {
                sont = 0;
                break;
            }
        }
        if (sont == 1)
        {
            fprintf(file, "%d\t", i);
            count++;
            if (count == 10)
            {
                fprintf(file, "\n");
                count =0;
            }
        }
    }
}
int main()
{
    FILE *file = fopen("So_nguyen_to.txt", "w");
    if (file == NULL)
    {
        printf("Error\n");
        return 1;
    }
    else
    {
        printf("Mo file thanh cong\n");
    }
    isPrime(file);
    fclose(file);
    return 0;
}