#include <stdio.h>

int main() {
    int n, found = 0;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (arr[i] % 2 != 0 && arr[i] % 5 == 0) {
            found = 1;
            break;
        }
    }

    if (found)
        printf("Co ton tai so le chia het cho 5");
    else
        printf("Khong co so le chia het cho 5");

    return 0;
}
