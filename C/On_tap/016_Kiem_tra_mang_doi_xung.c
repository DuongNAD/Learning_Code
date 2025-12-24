#include <stdio.h>

int main() {
    int n, isSymmetric = 1;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);

    for (int i = 0; i < n / 2; i++) {
        if (arr[i] != arr[n - 1 - i]) {
            isSymmetric = 0;
            break;
        }
    }

    if (isSymmetric)
        printf("Mang doi xung");
    else
        printf("Mang khong doi xung");

    return 0;
}
