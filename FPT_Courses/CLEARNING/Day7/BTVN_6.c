#include<stdio.h>

void inputArry(int arr[], int *n){
    printf("Nhap do dai cua mang n = ");
    scanf("%d", n);
    printf("Nhap gia tri cua mang\n");
    for(int i = 0;i<*n;i++){
        printf("arr[%d] = ",i);
        scanf("%d",&arr[i]);
    }
    printf("\n");
}

void printArry(int *arr, int *n ){
    printf("Cac phan tu cua mang la\n");
    for(int i = 0;i<*n;i++){
        printf("arr[%d] = %d\n",i,*(arr+i));
    }
}
int main (){
    int arr[100];
    int n;
    inputArry(arr,&n);
    printArry(arr,&n);
    return 0;
}