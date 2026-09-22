#include <stdio.h>
#include <ctype.h>
int main()
{
    char c;
    printf("Nhap mot ki tu: ");
    scanf("%c", &c);
    if (islower(c))
    {
        printf("Day la chu thuong\n");
    }
    else if (isupper(c))
    {
        printf("Day la chu in hoa\n");
    }
    else
    {
        printf("Nhap lai: ");
    }
    return 0;
}