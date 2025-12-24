#include <stdio.h>
#include <string.h>

int main() {
    char s[100];
    int i = 0;

    fgets(s, 100, stdin);
    s[strcspn(s, "\n")] = 0;

    while (s[i] != '\0') {
        if (s[i] >= 'A' && s[i] <= 'Z') {
            s[i] = s[i] + 32;
        }
        i++;
    }

    printf("%s", s);

    return 0;
}