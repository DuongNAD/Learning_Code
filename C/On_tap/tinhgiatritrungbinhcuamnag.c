#include <stdio.h>

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    int sum = 0;

    for (int i = 0; i < 5; i++) {
        sum += arr[i];
    }

    float average = (float)sum / 5;

    printf("Giá trị trung bình: %.2f\n", average);

    return 0;
}