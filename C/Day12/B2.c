// Bài 2. Viết một chương trình nhận vào một chuỗi và sử dụng con trỏ để xác
// định chuỗi nhập vào có phải phải chuỗi palindrome (viết theo chiều ngược, hay thuận đều giống nhau) hay không.

#include <stdio.h>
#include <string.h>

void Input(char *c, int size)
{
    printf("Nhap chuoi: ");
    fgets(c, size, stdin);
    size_t len = strlen(c);
    if (len > 0 && c[len - 1] == '\n')
    {
        c[len - 1] = '\0';
    }
}

void Output(const char *c)
{
    printf("Chuoi vua nhap: %s\n", c);
}


int Start_End(const char *c)
{
    const char *start = c;
    const char *end = c + strlen(c) - 1;

    while (start < end)
    {
        if (*start != *end)
        {
            return 0;
        }
        start++;
        end--;
    }
    return 1;
}

int main()
{
    char c[1000];

    char start[1000];
    Input(c, sizeof(c));
    Output(c);

    if (Start_End(c) == 0)
    {
        printf("Day khong phai la chuoi palindrome");
    }
    else if (Start_End(c) == 1)
    {
        printf("Day la chuoi palindrome");
    }
    return 0;
}