#include<stdio.h>
#include<ctype.h>

int main () {
    char chuoiso[100];
    char n;
    int i =0;
    do
    {
        printf("Nhap cac so n (n la so nguyen) = ");
        n= getchar();
        if (n != int(n) || isalpha(n) || ispunct(n))
        {
            printf("n phai la so nguyen");
        }
        else{
            chuoiso[i] = n;
            i++;
        }
    } while (n = '\n' || i<99);

    chuoiso[i] = '\0';

    printf("Ban da nhap chuoi so: %s\n", chuoiso);

    return 0;
}
