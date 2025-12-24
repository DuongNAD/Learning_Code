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
    for (int i = 0; i < size - 1; i++)
    {
        if (c[i] == ' ')
        {
            for (int j = i; j < size - 1; j++)
            {
                c[j] = c[j + 1];
            }
            size--;
            c[size] = '\0';
            i--;
        }
    }
    for (int i = 0; i < size; i++)
    {
        if (isupper(c[i]))
        {
            c[i] = tolower(c[i]);
        }
    }
    int visited[255] = {0};
    for (int i = 0; i < size; i++)
    {
        if (visited[i] == 0)
        {
            int count = 0;
            for (int j = i; j < size; j++)
            {
                if (c[i] == c[j])
                {
                    count++;
                    visited[j] = 1;
                }
            }
            printf("Ki tu %c xuat hien %d lan\n", c[i], count);
        }
    }
    return 0;
}