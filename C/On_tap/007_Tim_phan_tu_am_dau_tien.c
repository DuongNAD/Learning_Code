#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int arr[n];
    int found = 0;

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (!found && arr[i] < 0) {
            printf("Phan tu am dau tien: %d", arr[i]);
            found = 1;
        }
    }

    if (!found) printf("Khong co so am nao");
    return 0;
}
