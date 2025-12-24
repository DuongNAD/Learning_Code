#include <stdio.h>
#include <stdlib.h>

int absDiff(int a, int b) {
    return abs(a - b);
}

int main() {
    int n, maxDiff = 0;
    scanf("%d", &n);
    int a[n];

    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            int d = absDiff(a[i], a[j]);
            if (d > maxDiff) maxDiff = d;
        }
    }

    printf("Do lech lon nhat: %d", maxDiff);
    return 0;
}
