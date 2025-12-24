#include <stdio.h>

int main()
{
    int i = 1;
    int j = 1;
start:
    if (i > 10)
        return 0;

    printf("%d * %d = %d\t  ", i, j, i * j);
    j++;
    if (j > 10)
    {
        j = 1;
        i++;
        printf("\n");
    }
    goto start;
}
