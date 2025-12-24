#include <stdio.h>

int main() {
    int n, chan = 0, le = 0;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (arr[i] % 2 == 0) chan++;
        else le++;
    }

    if (chan == le)
        printf("So chan va le bang nhau");
    else
        printf("Khong bang nhau");

    return 0;
}
