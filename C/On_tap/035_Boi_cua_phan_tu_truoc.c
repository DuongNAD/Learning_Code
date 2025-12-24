#include <stdio.h>

int main() {
    int n, count = 0;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    for (int i = 1; i < n; i++) {
        if (arr[i - 1] != 0 && arr[i] % arr[i - 1] == 0) {
            count++;
        }
    }

    printf("So luong phan tu la boi cua phan tu dung truoc: %d", count);
    return 0;
}
