#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main()
{
    char c[100];
    printf("Nhap mang: ");
    fgets(c, sizeof(c), stdin);

    size_t size = strlen(c);
    if (size > 0 && c[size - 1] == '\n')
    {
        c[size - 1] = '\0';
        size--;
    }

    int startIndex = -1;
    int endIndex = -1;

    for (int i = 0; i < size; i++)
    {
        if (c[i] != ' ')
        {
            startIndex = i;
            break;
        }
    }

    for (int j = size - 1; j >= 0; j--)
    {
        if (c[j] != ' ')
        {
            endIndex = j;
            break;
        }
    }

    for (int i = startIndex; i <= endIndex; i++)
    {
        c[i] = tolower(c[i]);
    }

    if (islower(c[startIndex]))
    {
        c[startIndex] = toupper(c[startIndex]);
    }

    printf("\nHo va ten: ");
    for (int i = startIndex; i <= endIndex; i++)
    {
        if (c[i] != ' ')
        {
            printf("%c", c[i]);
        }
        if (c[i + 1] == ' ' && c[i] != ' ')
        {
            printf("%c", c[i + 1]);
        }
        if (c[i] == ' ' && c[i + 1] != ' ')
        {
            c[i + 1] = toupper(c[i + 1]);
        }
    }

    printf("\n");
    
    char *token = strtok(c + startIndex, " ");

    char ho[50] = "", ten[50] = "", dem[50] = "";

    if (token != NULL)                              // ho
    {
        strcpy(ho, token);
        token = strtok(NULL, " ");
    }

    char lastToken[50] = "";
    while (token != NULL)                           // dem
    {
        strcpy(lastToken, token);
        token = strtok(NULL, " ");
                                                    /*NULL làm tham số đầu tiên nghĩa là tiếp tục tách từ chuỗi đã xử lý trước đó.
                                                    " " là ký tự phân tách (khoảng trắng).
                                                    Hàm trả về con trỏ tới token tiếp theo trong chuỗi.*/
        if (token != NULL)
        {
            if (strlen(dem) > 0)
            {
                strcat(dem, " ");
            }
            strcat(dem, lastToken);
        }
    }

    strcpy(ten, lastToken);                         // ten

    printf("\nTen chuan hoa: ");
    printf("%s ", ten);
    if (strlen(dem) > 0)
    {
        printf("%s ", dem);
    }
    printf("%s", ho);

    return 0;
}