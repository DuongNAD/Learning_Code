#include <stdio.h>
#include<ctype.h>
int islower(char c) {
    return (c >= 'a' && c <= 'z') ? 1 : 0;
}

int isupper(char c) {
    return (c >= 'A' && c <= 'Z') ? 1 : 0;
}

int isalpha(char c) {
    return islower(c) || isupper(c);
}

int isdigit(char c) {
    return (c >= '0' && c <= '9') ? 1 : 0;
}

int isalnum(char c) {
    return isalpha(c) || isdigit(c);
}

int tolower(char c) {
    if (isupper(c)) {
        return c + 32;
    }
    return c;
}

int toupper(char c) {
    if (islower(c)) {
        return c - 32;
    }
    return c;
}

int main() {
    char c;

    printf("Nhap 1 ki tu: ");
    scanf("%c", &c);

    printf("islower('%c') = %d\n", c, islower(c));
    printf("isupper('%c') = %d\n", c, isupper(c));
    printf("isalpha('%c') = %d\n", c, isalpha(c));
    printf("isdigit('%c') = %d\n", c, isdigit(c));
    printf("isalnum('%c') = %d\n", c, isalnum(c));
    printf("tolower('%c') = %c\n", c, tolower(c));
    printf("toupper('%c') = %c\n", c, toupper(c));

    return 0;
}
