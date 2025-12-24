#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "apple";
    char str2[] = "banana";

    int result = strcmp(str1, str2); // So sánh str1 và str2

    if (result == 0) {
        printf("Hai chuỗi giống nhau.\n");
    } else if (result < 0) {
        printf("Chuỗi 1 nhỏ hơn chuỗi 2.\n");
    } else {
        printf("Chuỗi 1 lớn hơn chuỗi 2.\n");
    }

    return 0;
}