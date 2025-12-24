#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main()
{
    char c[100];
    printf("Nhap chuoi: ");
    fgets(c, sizeof(c), stdin);
    for (int i = 0; i < strlen(c); i++){
        if (islower(c[i]))
        {
            c[i] = c[i] - 32;
        }
    }
    printf("\n");
    printf("Chuoi chu hoa: \n");
    fputs(c, stdout);
    for (int i = 0; i < strlen(c); i++){
        if (isupper(c[i]))
        {
            c[i] = c[i] + 32;
        }
    }
    printf("\n");
    printf("Chuoi chu thuong: \n");
    fputs(c, stdout);
    return 0;
}