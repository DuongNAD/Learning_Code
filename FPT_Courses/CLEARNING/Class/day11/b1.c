#include <stdio.h>

int main() {
    char str[100];
    scanf("%s", str);

    int i = 0;
    int upperCount = 0;
    int lowerCount = 0;

    while (str[i] != '\0') {
        if (str[i] >= 'A' && str[i] <= 'Z') {
            upperCount++;
        }
        if (str[i] >= 'a' && str[i] <= 'z') {
            lowerCount++;
        }
        i++;
    }

    printf("Chu hoa = %d\n", upperCount);
    printf("Chu thuong = %d\n", lowerCount);

    return 0;
}