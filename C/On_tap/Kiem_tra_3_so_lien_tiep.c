#include <stdio.h>

int main() {
    int n, found = 0;
    scanf("%d", &n);
    int a[n];

    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    for (int i = 0; i < n - 2; i++) {
        if (a[i] == a[i + 1] && a[i + 1] == a[i + 2]) {
            found = 1;
            break;
        }
    }

    if (found)
        printf("Co 3 so lien tiep bang nhau");
    else
        printf("Khong co 3 so lien tiep bang nhau");

    return 0;
}
