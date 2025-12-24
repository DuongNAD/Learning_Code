#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char s[101];
    int count = 0;

    printf("Nhap chuoi S (toi da 100 ky tu):\n");
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = 0;

    for (int i = 0; i < strlen(s); i++) {
        char c = tolower(s[i]); // Chuy?n sang ch? thu?ng d? ki?m tra
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            count++;
        }
    }

    printf("OUTPUT:\n");
    printf("%d\n", count);

    printf("Press any key to continue . . .\n");
    getchar();
    getchar();

    return 0;
}