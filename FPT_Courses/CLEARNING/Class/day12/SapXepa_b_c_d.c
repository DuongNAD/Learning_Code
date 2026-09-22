#include <stdio.h>

int main() {
    char chars[4];
    char temp;
    int i, j;

    /* Doc 4 ky tu, luu y ' %c' de bo qua cac ky tu 'Enter' (newline) */
    for (i = 0; i < 4; i++) {
        scanf(" %c", &chars[i]);
    }

    /* Sap xep mang bang Bubble Sort */
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3 - i; j++) {
            if (chars[j] > chars[j + 1]) {
                temp = chars[j];
                chars[j] = chars[j + 1];
                chars[j + 1] = temp;
            }
        }
    }

    printf("OUTPUT:\n");
    
    /* In ket qua da sap xep voi dau cach */
    for (i = 0; i < 4; i++) {
        printf("%c ", chars[i]);
    }
    printf("\n");

    return 0;
}