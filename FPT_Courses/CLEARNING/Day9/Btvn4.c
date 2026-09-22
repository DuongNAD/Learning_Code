#include <stdio.h>
#include <string.h>
#include <ctype.h>
int main()
{
    char c[100];
    printf("Nhap chuoi: \n");
    fgets(c, sizeof(c), stdin);
    printf("Chuoi da nhap: \n");
    fputs(c, stdout);
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
            c[size] = 0;
            i--;
        }
    }
    int countN = 0;
    int countP = 0;
    for (int i = 0; i < size; i++)
    {
        if (isupper(c[i]))
        {
            c[i] = tolower(c[i]);
        }
        if (c[i] == 'u' || c[i] == 'e' || c[i] == 'o' || c[i] == 'a' || c[i] == 'i')
        {
            countN++;
        }
        else
            countP++;
    }
    printf("Nguyen am = %d\n", countN);
    printf("Phu am = %d\n", countP);
    return 0;
}