#include <stdio.h>

int main() {
    int n;
    int sum = 0;
    int count = 0;
    int i;

    scanf("%d", &n);

    for (i = n; i >= 0; i--) {
        if (i % 2 == 0) {
            sum += i;
            count++;
        }
        
        if (count == 3) {
            break;
        }
    }

    printf("OUTPUT:\n%d\n", sum);

    return 0;
}