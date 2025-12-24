#include <stdio.h>

int main() {
    int n, count = 0;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (i % 2 != 0 && arr[i] % 2 != 0) {
            count++;
        }
    }

    printf("So le o vi tri le: %d", count);
    return 0;
}
