#include <stdio.h>
int main()
{
    char c;
    printf("Nhap mot ki tu: ");
    scanf("%c", &c);
    if (c>='a'&&c<='z')
    {
        printf("%c", c - 32);
    }
    else if (c>='A'&&c<='Z')
    {
        printf("%c", c + 32);
    }
    else
    {
        printf("Error");
    }
    return 0;
}