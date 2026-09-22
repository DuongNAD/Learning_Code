#include<stdio.h>

void kTra(int array[],int n){
    int i;
    for(i = 0;i<n;i++){
        if(array[i] % 6 ==0){
            printf("Yes\t");
        }
        else{
            printf("No\t");
        }
    }
}


int main () {
    int array[100];
    int n, i;
    printf("Nhap so phan tu cua mang: ");
    scanf("%d",&n);
    for(i = 0;i<n;i++){
        printf("array[%d] = ",i);
        scanf("%d",&array[i]);
    }
    kTra(array,n);
    return 0;
}