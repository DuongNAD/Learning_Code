#include <stdio.h>

int main() {
    int arr[] = {1, 2, 3, 4, 2, 2, 5, 1, 2};
    int n = sizeof(arr) / sizeof(arr[0]);
    int count[100] = {0};
    int maxCount = 0, maxElement;
    for (int i = 0; i < n; i++) {
        count[arr[i]]++;
        if (count[arr[i]] > maxCount) {
            maxCount = count[arr[i]];
            maxElement = arr[i];
        }
    }
    printf("Phan tu xuat hien nhieu nhat: %d (%d lan)\n", maxElement, maxCount);
    return 0;
}