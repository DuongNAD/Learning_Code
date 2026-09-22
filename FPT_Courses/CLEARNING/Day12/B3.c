// Bài 3. Viết một chương trình quản lý nhân viên bằng C với mô tả sau:

// Data type
// Field
// Descriptio   n
// char
// name[20]
// Tên nhân viên
// char
// country[20]
// Quê quán
// int
// birthyear
// Năm sinh
// float
// salary
// Lương

// Tạo menu

// Employee management system
// 1. Input  Employee  |2. Display Employee Descending | 3. Save file   |  4. Analyze |   5. exit

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_EMPLOYEES 100

typedef struct
{
    char name[20];
    char country[20];
    int Sinh_nhat;
    float Luong;
} Employee;

Employee employees[MAX_EMPLOYEES];
int employeeCount = 0;

int isValidEmployee(int Sinh_nhat, float Luong)
{
    int nam_ht = 2025;
    int tuoi = nam_ht - Sinh_nhat;
    return (tuoi >= 18 && tuoi <= 60 && Luong >= 100 && Luong <= 500);
}

void inputEmployee()
{
    int So_Employees;
    printf("Enter the number of employees: ");
    scanf("%d", &So_Employees);

    for (int i = 0; i < So_Employees; i++)
    {
        Employee emp;

        printf("Enter name for employee (Ten) %d: ", i + 1);
        getchar();
        fgets(emp.name, sizeof(emp.name), stdin);
        emp.name[strcspn(emp.name, "\n")] = '\0';

        printf("Enter country for employee (Quoc tich) %d: ", i + 1);
        fgets(emp.country, sizeof(emp.country), stdin);
        emp.country[strcspn(emp.country, "\n")] = '\0';

        do
        {
            printf("Enter birth year (between 1965 and 2007) for employee (Nam sinh) %d: ", i + 1);
            scanf("%d", &emp.Sinh_nhat);
            printf("Enter salary (between 100 and 500) for employee (luong) %d: ", i + 1);
            scanf("%f", &emp.Luong);
        } while (!isValidEmployee(emp.Sinh_nhat, emp.Luong));

        employees[employeeCount++] = emp;
    }
}

int compareEmployeeName(const void *a, const void *b)
{
    return strcmp(((Employee *)a)->name, ((Employee *)b)->name);
}

void displayEmployees()
{
    qsort(employees, employeeCount, sizeof(Employee), compareEmployeeName);

    printf("\nEmployee List (Sorted by Name):\n");
    for (int i = 0; i < employeeCount; i++)
    {
        printf("%s | %s | %d | %.2f\n", employees[i].name, employees[i].country, employees[i].Sinh_nhat, employees[i].Luong);
    }
}

void saveToFile()
{
    char filename[100];
    printf("Enter the filename to save data: ");
    getchar();
    fgets(filename, sizeof(filename), stdin);
    filename[strcspn(filename, "\n")] = '\0';

    FILE *file = fopen(filename, "wb");
    if (file == NULL)
    {
        printf("Error\n");
        return;
    }

    fwrite(&employeeCount, sizeof(int), 1, file);
    fwrite(employees, sizeof(Employee), employeeCount, file);

    fclose(file);
    printf("Successfully.\n");
}

void analyze()
{
    char country[20];
    printf("Enter country name to analyze: ");
    getchar();
    fgets(country, sizeof(country), stdin);
    country[strcspn(country, "\n")] = '\0';

    int count = 0;
    for (int i = 0; i < employeeCount; i++)
    {
        if (strcmp(employees[i].country, country) == 0)
        {
            count++;
        }
    }

    printf("%d employees from %s\n", count, country);
}

int main()
{
    int luachon;
    do
    {
        printf("\nEmployee Management System\n");
        printf("1. Input Employee (Nhap): \n");
        printf("2. Display Employee Descending (Giam dan): \n");
        printf("3. Save File (luu): \n");
        printf("4. Analyze (Phan tich): \n");
        printf("5. Exit\n");
        printf("Lua chon (1 - 5): ");
        scanf("%d", &luachon);
        switch (luachon)
        {
        case 1:
            inputEmployee();
            break;
        case 2:
            displayEmployees();
            break;
        case 3:
            saveToFile();
            break;
        case 4:
            analyze();
            break;
        case 5:
            printf("Exit\n");
            break;
        default:
            printf("Lua chon khong hop le. Moi nhap lai\n");
        }
    } while (luachon != 5);

    return 0;
}