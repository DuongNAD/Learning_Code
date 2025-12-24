#include <stdio.h>
#include <limits.h>

int main() {
    int n, maxEven = INT_MIN;
    scanf("%d", &n);
    int arr[n];
    int found = 0;

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (arr[i] % 2 == 0 && arr[i] > maxEven) {
            maxEven = arr[i];
            found = 1;
        }
    }

    if (found)
        printf("So chan lon nhat: %d", maxEven);
    else
        printf("Khong co so chan nao");

    return 0;
}
