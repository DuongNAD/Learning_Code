#include <stdio.h>

int main() {
    int n, tich = 1, found = 0;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (arr[i] < 0) {
            tich *= arr[i];
            found = 1;
        }
    }

    if (found)
        printf("Tich cac so am: %d", tich);
    else
        printf("Khong co so am nao");

    return 0;
}
