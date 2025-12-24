#include <stdio.h>
#include <string.h>

struct Student {
    char id[10];
    char name[50];
    float mark;
};

int main() {
    struct Student list[100];
    int n, i;

    printf("Nhap so luong sinh vien: ");
    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        printf("\nNhap thong tin sinh vien thu %d:\n", i + 1);
        
        printf("ID: ");
        fflush(stdin);
        scanf("%[^\n]", list[i].id);

        printf("Ten: ");
        fflush(stdin);
        scanf("%[^\n]", list[i].name);

        printf("Diem: ");
        scanf("%f", &list[i].mark);
    }

    printf("\n--- Danh sach sinh vien ---\n");
    printf("%-10s %-30s %-10s\n", "ID", "Ten", "Diem");
    for (i = 0; i < n; i++) {
        printf("%-10s %-30s %-10.2f\n", list[i].id, list[i].name, list[i].mark);
    }

    return 0;
}