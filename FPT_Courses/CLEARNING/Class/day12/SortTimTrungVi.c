#include<stdio.h>

void SapXep(int array[], int n){
    int i,j;
    for(i = 0;i<n-1;i++){
        for(j= i +1;j<n;j++){
            if(array[i] > array[j]){
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
    }
}

double SearchMiddle (int array[], int n){

    if(n%2 == 1){
        return (double)array[(n-1)/2];
    }
    else{
        double middle1 = array[n/2];
        double middle2 = array[n/2 -1];
        return (double)((middle1 + middle2) /2);
    }

}

int main () {
    int n,i;
    int array[100];
    printf("Nhap so phan tu cua mang: ");
    scanf("%d",&n);
    for(i = 0;i<n;i++){
        printf("array[%d] = ",i);
        scanf("%d",&array[i]);
    }

    printf("Mang da sap xep:\n ");
    SapXep(array,n);
    for(i = 0;i<n;i++){
        printf("%d\t",array[i]);
    }
    printf("\n");
    double middle = SearchMiddle(array,n);
    printf("So trung vi: %.2f",middle);
    return 0;
}