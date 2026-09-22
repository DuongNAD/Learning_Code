#include <stdio.h>
#include <string.h>

struct Employee {
    char id[10];
    char name[50];
    int kpi; 
};

int main() {
    struct Employee list[100];
    int n, i;
    int passCount = 0;
    int failCount = 0;
    int kpi_standard = 80; 

    printf("Nhap so luong nhan vien: ");
    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        printf("\nNhap thong tin nhan vien thu %d:\n", i + 1);
        printf("ID: ");
        fflush(stdin);
        scanf("%[^\n]", list[i].id);
        printf("Ten: ");
        fflush(stdin);
        scanf("%[^\n]", list[i].name);
        printf("KPI (0-100): ");
        scanf("%d", &list[i].kpi);

        if (list[i].kpi >= kpi_standard) {
            passCount++;
        } else {
            failCount++;
        }
    }

    printf("\n--- Thong ke KPI (Chuan: %d) ---\n", kpi_standard);
    printf("So nhan vien dat KPI: %d\n", passCount);
    printf("So nhan vien khong dat KPI: %d\n", failCount);

    return 0;
}