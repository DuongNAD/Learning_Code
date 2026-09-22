#include <stdio.h>

int main() {
    int arr[7];
    int i, j, minIndex, temp;

    for (i = 0; i < 7; i++) {
        scanf("%d", &arr[i]);
    }

 
    for (i = 0; i < 6; i++) {

        minIndex = i;
        for (j = i + 1; j < 7; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }

        temp = arr[i];
        arr[i] = arr[minIndex];
        arr[minIndex] = temp;
    }

    printf("OUTPUT:\n");
    for (i = 0; i < 7; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}