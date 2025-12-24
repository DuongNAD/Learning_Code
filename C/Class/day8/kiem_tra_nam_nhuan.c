#include <stdio.h>

int main() {
    int year;
    printf("Enter a year: ");
    scanf("%d", &year);

    printf("\nOUTPUT:\n");
    // Một năm là năm nhuận nếu nó chia hết cho 400,
    // hoặc chia hết cho 4 nhưng không chia hết cho 100.
    if ((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0)) {
        printf("Leap Year\n");
    } else {
        printf("Not a Leap Year\n");
    }

    return 0;
}