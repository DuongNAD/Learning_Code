#include <stdio.h>
#include <string.h>

struct Movie {
    char title[100];
    int year;
    float rating;
};

struct Movie list[100];
int count = 0;

void addMovie() {
    if (count >= 100) {
        printf("Danh sach day!\n");
        return;
    }
    printf("\n--- Them phim moi ---\n");
    printf("Ten phim: ");
    fflush(stdin);
    scanf("%[^\n]", list[count].title);
    
    printf("Nam san xuat: ");
    scanf("%d", &list[count].year);
    
    printf("Danh gia (0-10): ");
    scanf("%f", &list[count].rating);
    
    count++;
    printf("Da them phim thanh cong!\n");
}

void displayMovies() {
    if (count == 0) {
        printf("\nChua co phim nao trong danh sach.\n");
        return;
    }
    printf("\n--- Danh sach phim (%d phim) ---\n", count);
    printf("%-30s %-10s %-10s\n", "Ten phim", "Nam", "Danh gia");
    printf("--------------------------------------------------\n");
    int i;
    for (i = 0; i < count; i++) {
        printf("%-30s %-10d %-10.1f\n", list[i].title, list[i].year, list[i].rating);
    }
}

int main() {
    int choice;

    do {
        printf("\n--- QUAN LY PHIM ---\n");
        printf("1. Them phim moi\n");
        printf("2. Hien thi danh sach phim\n");
        printf("0. Thoat chuong trinh\n");
        printf("Lua chon cua ban: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                addMovie();
                break;
            case 2:
                displayMovies();
                break;
            case 0:
                printf("Tam biet!\n");
                break;
            default:
                printf("Lua chon khong hop le. Vui long chon lai.\n");
        }
    } while (choice != 0);

    return 0;
}