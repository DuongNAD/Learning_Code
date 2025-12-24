#include <stdio.h>

int main() {
    int arr[5] = {1, 2, 3, 4, 5};

    printf("M?ng tru?c khi d?o ngu?c:\n");
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    for (int i = 0, j = 4; i < j; i++, j--) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    printf("M?ng sau khi d?o ngu?c:\n");
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}