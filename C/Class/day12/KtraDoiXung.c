#include <stdio.h>

int main() {
    int n;
    int arr[20];
    int i;
    int isSymmetric = 1; 


    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    for (i = 0; i < n / 2; i++) {
        if (arr[i] != arr[n - 1 - i]) {
            isSymmetric = 0; 
            break;           
        }
    }

    printf("OUTPUT:\n%d\n", isSymmetric);

    return 0;
}