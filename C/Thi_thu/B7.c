// Bài 7: Kiểm tra chuỗi đối xứng (10 điểm)
// Viết chương trình nhập vào một chuỗi và kiểm tra xem chuỗi đó có đối xứng không (ví dụ: "abba", "madam").

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    char *c = (char *)malloc(100 * sizeof(char));
    printf("Nhap chuoi:\n");
    fgets(c, 100, stdin);
    size_t size = strlen(c);
    if (size > 0 && c[size - 1] == '\n')
    {
        c[size - 1] = '\0';
        size--;
    }

    for (int i = 0; i < size / 2; i++)
    {
        if (c[i] != c[size - i - 1])
        {
            printf("Day la chuoi khong doi xung\n");
            free(c);
            return 0;
        }
    }
    printf("Day la chuoi doi xung\n");
    free(c);
    return 0;
}