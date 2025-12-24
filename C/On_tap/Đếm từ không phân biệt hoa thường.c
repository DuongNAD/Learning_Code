#include <stdio.h>

int isLeap(int year) {
    return (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0);
}

int getDays(int month, int isLeap) {
    if (month == 2) return isLeap ? 29 : 28;
    if (month == 4 || month == 6 || month == 9 || month == 11) return 30;
    return 31;
}

int main() {
    int year, n;
    scanf("%d %d", &year, &n);
    int months[n];
    
    for (int i = 0; i < n; i++) {
        scanf("%d", &months[i]);
    }
    
    int leap = isLeap(year);
    
    for (int i = 0; i < n; i++) {
        printf("%d ", getDays(months[i], leap));
    }
    
    return 0;
}