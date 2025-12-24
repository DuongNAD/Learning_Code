#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int a[n], visited[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
        visited[i] = 0;
    }

    printf("Cac phan tu lap lai:\n");
    for (int i = 0; i < n; i++) {
        if (visited[i]) continue;
        int count = 1;
        for (int j = i + 1; j < n; j++) {
            if (a[i] == a[j]) {
                visited[j] = 1;
                count++;
            }
        }
        if (count > 1) printf("%d xuat hien %d lan\n", a[i], count);
    }

    return 0;
}
