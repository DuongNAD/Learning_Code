#include <stdio.h>
#include<ctype.h>
int main()
{
    char c;
    printf("Nhap chu ma ASCII: ");
    scanf("%c", &c);
    if (isupper(c))
    {
        printf("Day la chu hoa");
    }
    else if (islower(c))
    {
        printf("Day la chu thuong");
    }
    else if (isdigit(c)){
        printf ("Day la so");
    }
    else
    {
        printf("Cac ki tu khac");
    }
    return 0;
}