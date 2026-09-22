#include <stdio.h>
#include<stdlib.h>

int main()
{
    int n;
    printf("Nhap so phan tu trong mang = ");
    scanf("%d", &n);
    int array[1000];
    for (int i = 1; i <= n; i++)
    {
        printf("Nhap so thu %d: ", i);
        scanf("%d", &array[i]);
    }
    printf("\n");
    printf("Hien thi mang: \n");
    for (int i = 0; i < n; i++)
    {
        printf("%d \t", array[i]);
    }
    printf("\n");
    printf("Mang da sap xep: \n");
    for (int i = 0; i < n - 1; i++) 
    {
        int min_idx = i; 
        for (int j = i + 1; j < n; j++) 
        {
            if (array[j] < array[min_idx]) {
                min_idx = j;
            }
        }
        if (min_idx != i) {
            int temp = array[i];
            array[i] = array[min_idx];
            array[min_idx] = temp;
        }
    }
    for (int i = 0; i < n; i++)
    {
        printf("%d\t", array[i]);
    }
    free(array);
    return 0;
}