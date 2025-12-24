#include <stdio.h>

int main() {
    int n, arr[100], minOdd = 1000000, maxOdd = -1, minOddIndex = -1, maxOddIndex = -1;
    printf("Nhap n: ");
    scanf("%d", &n);
    printf("Nhap mang: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (arr[i] % 2 != 0) {
            if (arr[i] < minOdd) {
                minOdd = arr[i];
                minOddIndex = i;
            }
            if (arr[i] > maxOdd) {
                maxOdd = arr[i];
                maxOddIndex = i;
            }
        }
    }
    if (minOddIndex != -1 && maxOddIndex != -1) {
        int temp = arr[minOddIndex];
        arr[minOddIndex] = arr[maxOddIndex];
        arr[maxOddIndex] = temp;
    }
    printf("Mang sau khi xu ly: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    return 0;
}