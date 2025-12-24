#include <stdio.h>

int main() {
    int n, i, j;
    double a[100], temp, median;
    
    // Nhập dữ liệu
    scanf("%d", &n);
    for(i = 0; i < n; i++) {
        scanf("%lf", &a[i]);
    }
    
    // Sắp xếp bằng bubble sort (đơn giản)
    for(i = 0; i < n-1; i++) {
        for(j = 0; j < n-i-1; j++) {
            if(a[j] > a[j+1]) {
                temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
            }
        }
    }
    
    // Tính median
    if(n % 2 == 1) {
        median = a[n/2];
    } else {
        median = (a[n/2 - 1] + a[n/2]) / 2.0;
    }
    
    // In kết quả
    printf("%.2f", median);
    
    return 0;
}