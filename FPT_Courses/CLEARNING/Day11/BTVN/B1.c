#include <stdio.h>

int main()
{
    FILE *file;
    file = fopen("bt1", "w");
    if (file == NULL)
    {
        printf("Error");
        return 1;
    }
    else
        printf("Mo file thanh cong\n");

    char s[100] = "DUong Anh 2006";
    fprintf(file,"%d\n%.2f\n%c\n%s\n", 100, 3.14, '@', s);
    fclose(file);
    return 0;
}