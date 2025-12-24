#include <stdio.h>

int main() {
    int n, maxCount = 0, res;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);

    for (int i = 0; i < n; i++) {
        int count = 1;
        for (int j = i + 1; j < n; j++) {
            if (arr[i] == arr[j]) count++;
        }
        if (count > maxCount) {
            maxCount = count;
            res = arr[i];
        }
    }

    printf("Phan tu xuat hien nhieu nhat: %d (%d lan)", res, maxCount);
    return 0;
}
