#include <stdio.h>
#include <string.h>

void nhap(char c[100])
{
    size_t size = strlen(c);
    printf("Nhap ten: ");
    fgets(c, 100, stdin);
    if (size > 0 && c[size - 1] == '\n')
    {
        c[size - 1] = '\0';
    }
}

void in(char c[100])
{
    printf("%s", c);
}

void ClearSpace(char c[100])
{
    char ho[20],ten[20],dem[20];
    size_t size =
     strlen (c);
    char *token = (strtok (c), " ");
    for (int i -0;i< size;i++){
        strcpy()
    }
}

int main()
{
    char c[100];
    nhap(c);
    clearSpace(c);
    return 0;
}