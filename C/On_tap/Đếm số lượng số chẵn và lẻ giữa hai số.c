#include <stdio.h>

int main() {
    int X, Y, even = 0, odd = 0;
    scanf("%d %d", &X, &Y);
    
    for (int i = X; i <= Y; i++) {
        if (i % 2 == 0) even++;
        else odd++;
    }
    
    printf("%d\n%d", even, odd);
    return 0;
}