#include <stdio.h>

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    int key = 3;
    int found = 0;

    for (int i = 0; i < 5; i++) {
        if (arr[i] == key) {
            printf("Phần tử %d được tìm thấy tại vị trí %d.\n", key, i);
            found = 1;
            break;
        }
    }

    if (!found) {
        printf("Phần tử %d không được tìm thấy.\n", key);
    }

    return 0;
}