#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "Lap trinh C rat thu vi";
    char longestWord[100] = "";
    char currentWord[100] = "";
    int i = 0, j = 0;
    while (str[i] != '\0') {
        if (str[i] != ' ') {
            currentWord[j++] = str[i];
        } else {
            currentWord[j] = '\0';
            if (strlen(currentWord) > strlen(longestWord)) {
                strcpy(longestWord, currentWord);
            }
            j = 0;
        }
        i++;
    }
    currentWord[j] = '\0';
    if (strlen(currentWord) > strlen(longestWord)) {
        strcpy(longestWord, currentWord);
    }
    printf("Tu dai nhat: %s\n", longestWord);
    return 0;
}