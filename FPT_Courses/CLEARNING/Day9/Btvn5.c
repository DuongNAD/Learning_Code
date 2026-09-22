#include <stdio.h>
#include <string.h>

int main()
{
    char K[100];
    char V[100];
    printf("Nhap chuoi K:  ");
    fgets(K, sizeof(K), stdin);
    printf("Nhap chuoi V: ");
    fgets(V, sizeof(V), stdin);

    size_t sizeK = strlen(K);
    if (sizeK > 0 && K[sizeK - 1] == '\n')
    {
        K[sizeK - 1] = '\0';   // thay ki tu thu 2 tu cuoi len = '\0' ( xuong dong ) - ki tu cuoi cung la '\n'
        sizeK--;                // giam phan tu trong chuoi di 1
    }

    size_t sizeV = strlen(V);
    if (sizeV > 0 && V[sizeV - 1] == '\n')
    {
        V[sizeV - 1] = '\0';
        sizeV--;
    }

    char *result = strstr(K, V);

    if (result != NULL)
    {
        printf("Ham K chua chuoi V\n");
    }
    else
    {
        printf("Ham K khong chua chuoi V\n");
    }
    return 0;
}