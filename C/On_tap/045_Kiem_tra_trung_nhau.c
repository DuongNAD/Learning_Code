#include <stdio.h>

int main() {
    int n, found = 0;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);

    for (int i = 0; i < n - 1 && !found; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] == arr[j]) {
                found = 1;
                break;
            }
        }
    }

    if (found)
        printf("Co phan tu trung nhau");
    else
        printf("Khong co phan tu trung nhau");

    return 0;
}
