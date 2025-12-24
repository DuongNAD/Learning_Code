#include <stdio.h>
#include <string.h>

void removeDuplicates(char str[]) {
    int len = strlen(str);
    int index = 0;
    for (int i = 0; i < len; i++) {
        int j;
        for (j = 0; j < index; j++) {
            if (str[i] == str[j]) {
                break;
            }
        }
        if (j == index) {
            str[index++] = str[i];
        }
    }
    str[index] = '\0';
}

int main() {
    char str[] = "programming";
    removeDuplicates(str);
    printf("Chuoi sau khi loai bo trung lap: %s\n", str);
    return 0;
}