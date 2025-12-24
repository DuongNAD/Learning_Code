#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main()
{
    char c[100];
    printf("Nhap mang: ");
    fgets(c, sizeof(c), stdin);
    size_t size = strlen(c);
    if (size > 0 && c[size - 1] == '\n')
    {
        c[size - 1] = '\0';
        size--;
    }

    int startIndex = -1;
    int endIndex = -1;
    for (int i = 0; i < size; i++)
    {
        if (c[i] != ' ')
        {
            startIndex = i;
            break;
        }
    }
    for (int i = size - 1; i >= 0; i--)
    {
        if (c[i] != ' ')
        {
            endIndex = i;
            break;
        }
    }
    for (int i = startIndex; i <= endIndex; i++)
    {
        c[i] = tolower(c[i]);
    }

    if (islower(c[startIndex]))
    {
        c[startIndex] = toupper(c[startIndex]);
    }

    for (int i = startIndex; i <= endIndex; i++)
    {
        if (c[i] != ' ')
        {
            printf("%c", c[i]);
        }
        if (c[i] != ' ' && c[i + 1] == ' ')
        {
            printf("%c", c[i + 1]);
        }
        if (c[i] == ' ' && c[i + 1] != ' ')
        {
            c[i + 1] = toupper(c[i + 1]);
        }
    }

    return 0;
}