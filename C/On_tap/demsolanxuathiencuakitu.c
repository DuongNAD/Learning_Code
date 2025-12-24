#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "hello world";
    char ch = 'l';
    int count = 0;

    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] == ch) {
            count++;
        }
    }

    printf("Ký tự '%c' xuất hiện %d lần.\n", ch, count);

    return 0;
}