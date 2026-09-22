#include <stdio.h>
#include <string.h>

struct Book {
    char isbn[20];
    char title[100];
    char author[50];
};

int main() {
    struct Book library[3] = {
        {"978-0321765723", "The C Programming Language", "Kernighan & Ritchie"},
        {"978-0321563842", "Effective C++", "Scott Meyers"},
        {"978-0132354181", "Clean Code", "Robert C. Martin"}
    };
    int n = 3;
    char searchTitle[100];
    int found = 0;
    int i;

    printf("Nhap ten sach can tim: ");
    fflush(stdin);
    scanf("%[^\n]", searchTitle);

    printf("\nDang tim kiem...\n");

    for (i = 0; i < n; i++) {
        if (strcmp(library[i].title, searchTitle) == 0) {
            printf("Tim thay sach:\n");
            printf("ISBN: %s\n", library[i].isbn);
            printf("Tieu de: %s\n", library[i].title);
            printf("Tac gia: %s\n", library[i].author);
            found = 1;
            break;
        }
    }

    if (found == 0) {
        printf("Khong tim thay sach voi tieu de '%s'\n", searchTitle);
    }

    return 0;
}