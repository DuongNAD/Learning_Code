#include <stdio.h>

int main() {
    int n, found = 0;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);

    for (int i = 0; i < n - 1; i++) {
        int isLarger = 1;
        for (int j = i + 1; j < n; j++) {
            if (arr[i] <= arr[j]) {
                isLarger = 0;
                break;
            }
        }
        if (isLarger) {
            printf("Phan tu thoa dieu kien: %d", arr[i]);
            found = 1;
            break;
        }
    }

    if (!found) printf("Khong co phan tu nao thoa man");
    return 0;
}
