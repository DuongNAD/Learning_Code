// Bài 6: Chuẩn hóa tên (10 điểm)
// Viết chương trình nhập vào họ tên (có khoảng trắng), sau đó chuẩn hóa tên theo dạng "Nguyen Van A" (viết hoa chữ cái đầu mỗi từ, còn lại viết thường).

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
    char *c = (char *)malloc(100 * sizeof(char));
    printf("Nhap ten muon chuan hoa: \n");
    fgets(c, 100, stdin);
    printf("\n");
    size_t size = strlen(c);
    if (size > 0 && c[size - 1] == '\n')
    {
        c[size - 1] = '\0';
    }
    int startDex = 0;
    int endDex = 0;
    for (int i = 0; i < size - 1; i++)
    {
        if (c[i] != ' ')
        {
            startDex = i;
            break;
        }
    }

    for (int i = size; i >= 0; i--)
    {
        if (c[i] != ' ')
        {
            endDex = i;
            break;
        }
    }
    for (int i = startDex; i <= endDex; i++)
    {
        c[i] = tolower(c[i]);
    }
    c[startDex] = toupper(c[startDex]);

    for (int i = startDex; i < +endDex; i++)
    {

        if (c[i] != ' ')
        {
            printf("%c", c[i]);
        }
        if (c[i] == ' ' && c[i + 1] != ' ')
        {
            printf("%c", c[i]);
        }
        if (c[i] == ' ' && c[i + 1] != ' ')
        {
            c[i + 1] = toupper(c[i + 1]);
        }
    }
    free(c);
    return 0;
}