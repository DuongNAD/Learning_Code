#include <stdio.h>
#include <math.h>

int isPerfectSquare(int n) {
    int root = sqrt(n);
    return root * root == n;
}

int main() {
    int n, found = 0;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (!found && isPerfectSquare(arr[i])) {
            printf("So chinh phuong dau tien: %d", arr[i]);
            found = 1;
        }
    }

    if (!found) printf("Khong co so chinh phuong nao");
    return 0;
}
