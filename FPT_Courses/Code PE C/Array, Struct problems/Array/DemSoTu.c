#include <stdio.h>
#include <string.h>

int countWords(char s[]) {
    int count = 0;
    int i;
    int len = strlen(s);

    if (len == 0) {
        return 0;
    }

    for (i = 0; i < len; i++) {
        if (s[i] != ' ') {
            if (i == 0 || s[i - 1] == ' ') {
                count++;
            }
        }
    }
    
    return count;
}

int main() {

    char s[101]; 
    scanf("%[^\n]", s);
    
    int result = countWords(s);
    
    printf("%d\n", result);
    
    return 0;
}