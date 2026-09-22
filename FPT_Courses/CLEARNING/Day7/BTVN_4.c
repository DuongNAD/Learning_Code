#include<stdio.h>
void nhapmang (int arr[],int *n){
    printf("Nhap so phan tu trong mang: ");
    scanf("%d",n);
    for(int i=0;i<*n;i++){
        printf("arr[%d] = ",i);
        scanf("%d",&arr[i]);
    }
}

void deleteElement (int arr[],int *n,int i){
    if(i< 0||i>=*n){
        printf("Vi tri xoa khong hop le\n");
        return;
    }
    for(int j =i;j<*n-1;j++){
        arr[j] = arr[j+1];
    }
    (*n)--;
    printf("Da xoa phan tu o vi tri %d\n",i);
}

int main (){
    int arr[100];
    int n,i,j;
    nhapmang(arr, &n);
    printf("Nhap vi tri can xoa: ");
    scanf("%d",&i);
    deleteElement(arr,&n,i);
    for(int j =0;j<n;j++){
        printf("arr[%d] = %d\n",j,arr[j]);
    }
    return 0;
}