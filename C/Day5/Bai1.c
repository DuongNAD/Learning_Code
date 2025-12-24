#include <stdio.h>
int main()
{
    int i = 1, j = 1;
start:
    if (i > 10)
        return 0;
    printf("%d * %d = %d", i, j, i * j);
    i++;
    if (j > 10)
    {
        j = 1;
        i++;
        printf("\n");
    }
    goto start;
}