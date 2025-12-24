#include <stdio.h>

int main() {
    int arr[] = {4, 6, 8, 9, 10, 11, 12};
    int n = sizeof(arr) / sizeof(arr[0]);
    int found = 0;
    for (int i = 0; i < n; i++) {
        if (kiemTraNguyenTo(arr[i])) {
            printf("So nguyen to dau tien trong mang la %d tai vi tri %d.\n", arr[i], i);
            found = 1;
            break;
        }
    }
    if (!found) {
        printf("Khong co so nguyen to trong mang.\n");
    }
    return 0;
}