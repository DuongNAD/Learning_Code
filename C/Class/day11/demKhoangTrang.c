#include <stdio.h>
#include <ctype.h>

int main() {
    char s[1000];
    int count = 0;
    int i = 0;

    printf("Moi Anh nhap vao mot chuoi: ");
    fgets(s, sizeof(s), stdin);

    while (s[i] != '\0') {
        if (!isalpha(s[i])) {
            count++;
        }
        i++;
    }

    printf("So luong chu so trong chuoi la: %d\n", count);

    return 0;
}