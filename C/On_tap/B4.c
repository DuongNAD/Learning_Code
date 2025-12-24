#include <stdio.h>
#include <string.h>

void deleteElement(char c[])
{

    printf("Nhap mang c: \n");
    fgets(c, 100, stdin);
    size_t size = strlen(c);
    if (size > 0 && c[size - 1] == '\n')
    {
        c[size - 1] = '\0';
        size--;
    }

    int delete;

    printf("Nhap voi tri muon xoa: ");
    scanf("%d", &delete);
    getchar();
    if (delete < 0 || delete >= size - 1)
    {
        printf("Vi tri xoa khong hop le!\n");
        return;
    }

    for (int i = delete; i < size; i++)
    {
        c[i] = c[i + 1];
    }
    size--;
    c[size] = '\0';
    
    printf("chuoi sau khi xoa:\n %s", c);
}

int main()
{
    char c[100];
    deleteElement(c);
    return 0;
}