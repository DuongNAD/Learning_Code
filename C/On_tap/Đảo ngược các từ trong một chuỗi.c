#include <stdio.h>
#include <string.h>

void reverseWords(char str[]) {
    int start = 0, end = 0;
    int len = strlen(str);
    for (int i = 0; i <= len; i++) {
        if (str[i] == ' ' || str[i] == '\0') {
            end = i - 1;
            for (int j = start; j < end; j++, end--) {
                char temp = str[j];
                str[j] = str[end];
                str[end] = temp;
            }
            start = i + 1;
        }
    }
}

int main() {
    char str[] = "Lap trinh C rat thu vi";
    reverseWords(str);
    printf("Chuoi sau khi dao nguoc tu: %s\n", str);
    return 0;
}