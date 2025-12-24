#include <stdio.h>

int main()
{
    FILE *file = fopen("bt1", "r");
    int n;
    float m;
    char a, b[50], c[50];
    if (file == NULL)
    {
        printf("Error\n");
    }
    else
    {
        printf("Mo file thanh cong\n");
    }
    if (fscanf(file, "%d\n%f\n%c\n%s\n%s", &n, &m, &a, b, c) == 5)
    {
        printf("Du lieu tu file: \n");
        printf("%d\n%.2f\n%c\n%s\n%s\n", n, m, a, b, c);
    }
    else
    {
        printf("Error: khong the doc du lieu tu file\n");
    }
    fclose(file);
    return 0; 
}