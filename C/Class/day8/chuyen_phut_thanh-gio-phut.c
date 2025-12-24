#include <stdio.h>

int main() {
    int totalMinutes, hours, minutes;
    printf("Enter total minutes: ");
    scanf("%d", &totalMinutes);

    hours = totalMinutes / 60;
    minutes = totalMinutes % 60;

    printf("\nOUTPUT:\n");
    printf("Hours: %d\n", hours);
    printf("Minutes: %d\n", minutes);

    return 0;
}