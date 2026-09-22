#include <stdio.h>

double averageArray(int a[], int n) {
    if (n == 0) {
        return 0.0;
    }
    
    int sum = 0;
    int i;
    for (i = 0; i < n; i++) {
        sum += a[i];
    }
    
    return (double)sum / n;
}

double averageOddAboveMean(int a[], int n) {
    double mean = averageArray(a, n);
    
    int sumOddAbove = 0;
    int countOddAbove = 0;
    int i;
    
    for (i = 0; i < n; i++) {
        if (a[i] % 2 != 0 && a[i] > mean) {
            sumOddAbove += a[i];
            countOddAbove++;
        }
    }
    
    if (countOddAbove == 0) {
        return 0.0;
    }
    
    return (double)sumOddAbove / countOddAbove;
}

int main() {
    int n;
    int a[100];
    int i;

    scanf("%d", &n);
    
    for (i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    
    double result = averageOddAboveMean(a, n);
    
    printf("%.2f\n", result);
    
    return 0;
}