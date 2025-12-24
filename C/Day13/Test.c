#include <stdio.h>
#include <string.h>

void Input(char c[100])
{
    printf("Nhap mang: ");

    size_t size = strlen(c);
    if (size > 0 && c[size - 1] == '\n')
    {
        c[size - 1] = '\0';
    }
    fgets(c, size, stdin);
    getchar();
}

void Output(char c[])
{
    printf("Mang da nhap: \n");

    scanf("%s",c);
}
int main()
{
    char c[100];
    Input(c);
    Output(c);
    return 0;
}