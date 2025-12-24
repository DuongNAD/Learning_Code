#include <stdio.h>
#include <string.h>

void inputArray(char c[], int size)
{
    printf("Nhap mang: \n");
    fgets(c, size, stdin);
    printf("\n");

    size_t len = strlen(c);

    if (len > 0 && c[len - 1] == '\n')
    {
        c[len - 1] = '\0';
    }
}

void outputArray(char c[])
{
    printf("Mang da nhap:\n");
    fputs(c, stdout);
}
int main()
{
    char c[100];
    inputArray(c, sizeof(c));
    outputArray(c);
    return 0;
}