#include <stdio.h>
#include <limits.h>

int main() {
    int n, maxNeg = INT_MIN, found = 0;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (arr[i] < 0 && arr[i] > maxNeg) {
            maxNeg = arr[i];
            found = 1;
        }
    }

    if (found)
        printf("So am lon nhat: %d", maxNeg);
    else
        printf("Khong co so am nao");

    return 0;
}
