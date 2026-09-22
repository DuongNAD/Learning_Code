#include <stdio.h>

int main() {
    int n,i,j, sum =0;

    do {
        scanf("%d",&n);
        if (n <=1) {
            printf("n need >1\n");
        }
    }
    while(n <=1);

    int matrix[100][100];

    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }

    printf("\nOUTPUT\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }

    for (i = 0; i < n; i++) {
        sum += matrix[i][(n-1) -i];
    }
    printf("\n%d\n", sum);
}