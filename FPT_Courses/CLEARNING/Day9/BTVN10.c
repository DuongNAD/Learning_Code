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
    char arr[100];
    int k = 0;
    for (int i = startIndex; i <= endIndex; i++)
    {
        if (c[i] != ' ')
        {
            arr[k++] = c[i];
        }
        if (c[i] != ' ' && c[i + 1] == ' ')
        {
            arr[k++] = c[i + 1];
        }
    }
    arr[k] = '\0';
    for (int i = 0; i < k; i++)
    {
        arr[i] = tolower(arr[i]);
    }

    char *token = strtok(arr, " ");
    char lastToken[50];
    char ten[50] = "", ho[50] = "", dem[50] = "";

    if (token != NULL)
    {
        strcpy(ho, token);
        token = strtok(NULL, " ");
    }

    while (token != NULL)
    {
        strcpy(lastToken, token);
        token = strtok(NULL, " ");

        if (token != NULL)
        {
            if (strlen(dem) > 0)
            {
                strcat(dem, " ");
            }
            strcat(dem, lastToken);
        }
    }
    strcpy(ten, lastToken);

    char a[10]="",b[10]="",z[100]="";

    if(strlen(ho)>0){
        a[0]=ho[0];
        a[1]='\0';
    }


    if (strlen(dem) > 0)
{
    b[0] = tolower(dem[0]);
    b[1] = '\0'; 

    for (int i = 0; i < strlen(dem); i++)
    {
        if (dem[i] == ' ' && dem[i + 1] != ' ')
        {
            z[0] = tolower(dem[i + 1]);
            z[1] = '\0'; 
            break;
        }
    }
}

    printf("%s%s%s%s@aptech.com.vn\n", ten, a,b,z);

    return 0;
}