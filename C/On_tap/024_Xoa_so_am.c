#include <stdio.h>

int main() {
    int n, j = 0;
    scanf("%d", &n);
    int arr[n], result[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (arr[i] >= 0) {
            result[j++] = arr[i];
        }
    }

    printf("Mang sau khi xoa so am:\n");
    for (int i = 0; i < j; i++) {
        printf("%d ", result[i]);
    }

    return 0;
}
