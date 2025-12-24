#include <stdio.h>
#include <string.h>

int main() {
    char str1[50] = "Hello, ";
    char str2[] = "world!";

    strcat(str1, str2);

    printf("Chuoi sau khi noi: %s\n", str1);

    return 0;
}