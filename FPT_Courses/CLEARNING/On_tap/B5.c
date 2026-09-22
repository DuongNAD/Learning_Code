#include <stdio.h>
#include <string.h>

void insertElement(char c[])
{
    printf("Nhap chuoi c: \n");
    fgets(c, 100, stdin);
    size_t size = strlen(c);
    if (size > 0 && c[size - 1] == '\n')
    {
        c[size - 1] = '\0';
        size--;
    }

    int insert;
    printf("Nhap vi tri muon them: ");
    scanf("%d", &insert);
    getchar();
    if (insert < 0 || insert >= size - 1)
    {
        printf("Error");
        return;
    }
    char value;
    printf("Nhap gia tri muon them: ");
    scanf("%c", &value);

    for (int i = size; i >= insert; i--)
    {
        c[i + 1] = c[i];
    }
    size++;
    c[insert] = value;
    c[size + 1] = '\0';
    printf("Chuoi sau khi chen: %s", c);
}

int main()
{
    char c[100];
    insertElement(c);
    return 0;
}