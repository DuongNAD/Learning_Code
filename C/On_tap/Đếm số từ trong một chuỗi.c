#include <stdio.h>
#include <string.h>

int countWords(char str[]) {
    int count = 0, i = 0;
    while (str[i] != '\0') {
        if (str[i] != ' ' && (str[i + 1] == ' ' || str[i + 1] == '\0')) {
            count++;
        }
        i++;
    }
    return count;
}

int main() {
    char str[] = "Lap trinh C rat thu vi";
    printf("So tu trong chuoi: %d\n", countWords(str));
    return 0;
}