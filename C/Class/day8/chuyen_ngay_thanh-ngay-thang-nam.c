#include <stdio.h>

int main() {
    int totalDays, years, weeks, remainingDays;
    printf("Enter total number of days: ");
    scanf("%d", &totalDays);

    years = totalDays / 365;
    remainingDays = totalDays % 365;
    weeks = remainingDays / 7;
    remainingDays = remainingDays % 7;

    printf("\nOUTPUT:\n");
    printf("Years: %d\n", years);
    printf("Weeks: %d\n", weeks);
    printf("Days: %d\n", remainingDays);

    return 0;
}