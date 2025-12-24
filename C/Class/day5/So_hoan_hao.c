#include <stdio.h>
#include <math.h>

int main() {
    int n;	
    printf("Nhap n = ");
    scanf("%d", &n);

    if (n <= 1) {
        printf("NO\n");
        return 0;
    }


	long long sum = 0;

    for (int i = 1; i <= n/2; i++) {

        if (n % i == 0) {
            sum = sum +i;
            }
        }

    if (sum == n) {
        printf("YES\n");
    } else {
        printf("NO\n");
    }

    return 0;
}