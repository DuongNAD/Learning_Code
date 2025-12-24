#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "This is a sample string.";
    char find[] = "sample";
    char replace[] = "test";
    char newStr[100];
    char *pos = strstr(str, find);
    if (pos != NULL) {
        strncpy(newStr, str, pos - str);
        newStr[pos - str] = '\0';
        strcat(newStr, replace);
        strcat(newStr, pos + strlen(find));
        printf("New string: %s\n", newStr);
    } else {
        printf("Word not found.\n");
    }
    return 0;
}