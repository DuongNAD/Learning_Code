#include <stdio.h>
#include <string.h>
#include <ctype.h>

void toLowerString(char *str) {
    for (int i = 0; str[i]; i++) {
        str[i] = tolower(str[i]);
    }
}

int main() {
    char sentence[1000], word[100];
    fgets(sentence, 1000, stdin);
    scanf("%s", word);
    
    toLowerString(sentence);
    toLowerString(word);
    
    char *token = strtok(sentence, " \n");
    int count = 0;
    
    while (token != NULL) {
        if (strcmp(token, word) == 0) {
            count++;
        }
        token = strtok(NULL, " \n");
    }
    
    printf("%d", count);
    return 0;
}