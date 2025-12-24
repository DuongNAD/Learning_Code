#include <stdio.h>

int main() {
    int m;
    scanf("%d", &m);
    
    for (int i = m; i >= 1; i--) {
        if (m % i == 0) {
            printf("%d", i);
        }
    }
    
    return 0;
}