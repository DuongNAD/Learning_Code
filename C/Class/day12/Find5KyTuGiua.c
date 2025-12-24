#include <stdio.h>
#include <string.h>

int main() {
    char str[21];
    int len, midIndex, startIndex, endIndex, i;

    scanf("%s", str);

    len = strlen(str);
    
    midIndex = len / 2;
    
    startIndex = midIndex - 2;
    endIndex = midIndex + 2;

    printf("OUTPUT:\n");
    
    for (i = startIndex; i <= endIndex; i++) {
        printf("%c", str[i]);
    }
    printf("\n");

    return 0;
}