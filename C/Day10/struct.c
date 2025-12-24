#include <stdio.h>
#include <string.h>

int getInteger(char message[50], int min, int max, char error[50])
{
    int number;
    while (1)
    {
        printf("%s", message);
        if (scanf("%d", &number) == 1)
        {
            if (number >= min && number < max)
            {
                return number;
            }
            else
            {
                printf("Error");
            }
        }
        else
        {
            printf("number must be range: %d -> %d", min, max);
            while (getchar() != '\n')
                ;
        }
    }
}

int main()
{
    int min = 1, max = 10;
    char message[] = "Please enter a number between 1 and 10: ";
    char error[] = "Error: Number must be in the range of 1 to 10.";

    int number = getInteger(message, min, max, error); // Gọi hàm nhập số
    printf("You entered: %d\n", number);               // Hiển thị kết quả

    return 0;
}