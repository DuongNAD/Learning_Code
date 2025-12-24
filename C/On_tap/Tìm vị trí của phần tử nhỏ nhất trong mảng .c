#include <stdio.h>

int demPhanTuLonHonTrungBinh(float arr[], int n) {
    float sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    float trungBinh = sum / n;
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] > trungBinh) {
            count++;
        }
    }
    return count;
}

int main() {
    float arr[] = {2.5, 4.0, 1.8, 3.2, 5.1};
    int n = sizeof(arr) / sizeof(arr[0]);
    printf("So luong phan tu lon hon gia tri trung binh: %d\n", demPhanTuLonHonTrungBinh(arr, n));
    return 0;
}