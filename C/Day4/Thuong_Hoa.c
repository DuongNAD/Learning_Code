#include <stdio.h>
int main()
{
    char c;
    printf("Nhap vao ki tu: ");
    scanf("%c", &c);
    if (c >= 'a' && c <= 'z')
    {
        printf("Chu hoa la: %c", c - 32);
    }
    else if (c >= 'A' && c <= 'Z')
    {
        printf("Chu thuong la: %c", c + 32);
    }
    else
    {
        printf("Error");
    }
    return 0;
}