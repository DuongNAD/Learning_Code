#include <stdio.h>
#include<ctype.h>
int main()
{
    char c;
    printf("Nhap vao mot ki tu: ");
    scanf("%c", &c);
    (islower(c)) ? printf("%c", c - 32) : (isupper(c)) ? printf("Day la ki tu in hoa ")
                                                                           : printf("Error");
    return 0;
}