#include <stdio.h>

int isLeapYear(int year) {
    if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
        return 1;
    } else {
        return 0;
    }
}

int main() {
    int year;
    printf("Nhap nam: ");
    scanf("%d", &year);
    if (isLeapYear(year)) {
        printf("%d la nam nhuan.\n", year);
    } else {
        printf("%d khong la nam nhuan.\n", year);
    }
    return 0;
}