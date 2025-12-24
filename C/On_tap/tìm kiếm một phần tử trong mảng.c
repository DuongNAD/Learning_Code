#include <stdio.h>

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    int key = 3;
    int found = 0;

    for (int i = 0; i < n; i++) {
        if (arr[i] == key) {
            printf("Phan tu %d duoc tim thay tai vi tri %d\n", key, i);
            found = 1;
            break;
        }
    }

    if (!found) {
        printf("Phan tu %d khong duoc tim thay trong mang\n", key);
    }

    return 0;
}