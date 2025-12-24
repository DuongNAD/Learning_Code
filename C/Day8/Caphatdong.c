#include<stdio.h>
#include<stdlib.h>

int main () {
    int arr[100];
    int n;
    printf("nhap kich thuoc mang ");
    scanf("%d",&n);
    int *p;
    p = (int*) malloc(n * sizeof(int));

    char *q;
    q = (char*) malloc(n * sizeof(char));

    int *q = (int*) calloc (100, sizeof(int));
    realloc(q,200 * sizeof(int));
    free(q);
    free (p);

return 0;
}