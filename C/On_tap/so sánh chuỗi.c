#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "apple";
    char str2[] = "banana";

    int result = strcmp(str1, str2);

    if (result == 0) {
        printf("Hai chuoi giong nhau.\n");
    } else if (result < 0) {
        printf("Chuoi 1 nho hon chuoi 2.\n");
    } else {
        printf("Chuoi 1 lon hon chuoi 2.\n");
    }

    return 0;
}