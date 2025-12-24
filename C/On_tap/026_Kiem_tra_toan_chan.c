#include <stdio.h>

int main() {
    int n, isAllEven = 1;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (arr[i] % 2 != 0) {
            isAllEven = 0;
            break;
        }
    }

    if (isAllEven)
        printf("Mang toan so chan");
    else
        printf("Mang co so le");

    return 0;
}
