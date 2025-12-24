#include <stdio.h>

int main() {
    int n, count = 0;
    scanf("%d", &n);
    int arr[n], visited[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        visited[i] = 0;
    }

    for (int i = 0; i < n; i++) {
        if (visited[i]) continue;
        int freq = 1;
        for (int j = i + 1; j < n; j++) {
            if (arr[i] == arr[j]) {
                freq++;
                visited[j] = 1;
            }
        }
        if (freq > 1) count++;
    }

    printf("So phan tu trung lap: %d", count);
    return 0;
}
