#include <stdio.h>
#include <ctype.h>
#include <string.h>

void chuanhoa(char arr[], FILE *file1)
{
    size_t size = strlen(arr);
    int StartDex = 0;
    int EndDex = size - 1;

    for (int i = 0; i < size; i++)
    {
        arr[i] = tolower(arr[i]);
    }

    if (size > 0 && arr[size - 1] == '\n')
    {
        arr[size - 1] = '\0';
        size--;
    }

    for (int i = 0; i < size; i++)
    {
        if (arr[i] != ' ')
        {
            StartDex = i;
            arr[StartDex] = toupper(arr[StartDex]);
            break;
        }
    }

    for (int i = EndDex; i >= 0; i++)
    {
        if (arr[i] != ' ')
        {
            EndDex = i;
            break;
        }
    }

    for (int i = StartDex; i <= EndDex; i++)
    {
        if (arr[i] != ' ')
        {
            fprintf(file1, "%c", arr[i]);
        }
        else if (arr[i] == ' ' && arr[i + 1] != ' ' && i + 1 <= EndDex)
        {
            arr[i + 1] = toupper(arr[i + 1]);
            fprintf(file1, "%c", arr[i]);
        }
    }
    fprintf(file1, "\n");
}

int main()
{
    char arr[100];
    int n;
    FILE *file = fopen("sinhvien.txt", "r");
    FILE *file1 = fopen("sinhvien_out.txt", "w");
    if (file == NULL)
    {
        printf("Error");
        return 1;
    }
    fscanf(file, "%d\n", &n);

    for (int i = 0; i < n; i++)
    {
        fgets(arr, sizeof(arr), file);
        chuanhoa(arr, file1);
    }
    fclose(file);
    fclose(file1);
    printf("Da chuan hoa va ghi vao sinhvien_out.txt");
    return 0;
}