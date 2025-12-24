#include <stdio.h>
#include <limits.h>

int main() {
    int n, maxOdd = INT_MIN, found = 0;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (arr[i] % 2 != 0 && arr[i] > maxOdd) {
            maxOdd = arr[i];
            found = 1;
        }
    }

    if (found)
        printf("So le lon nhat: %d", maxOdd);
    else
        printf("Khong co so le nao");

    return 0;
}
