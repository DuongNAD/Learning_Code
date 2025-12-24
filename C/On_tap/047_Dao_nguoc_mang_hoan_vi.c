#include <stdio.h>

int main() {
    int n, temp;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);

    for (int i = 0; i < n / 2; i++) {
        temp = arr[i];
        arr[i] = arr[n - 1 - i];
        arr[n - 1 - i] = temp;
    }

    printf("Mang sau khi dao nguoc:\n");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);

    return 0;
}
