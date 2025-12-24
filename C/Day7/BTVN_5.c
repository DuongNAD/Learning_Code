 #include<stdio.h>
void nhapmang (int arr[],int *n){
    printf("Nhap so phan tu trong mang: ");
    scanf("%d",n);
    for(int i=0;i<*n;i++){
        printf("arr[%d] = ",i);
        scanf("%d",&arr[i]);
    }
}
void insertElement (int arr[],int *n,int i,int them){
    if(i< 0||i>=*n){
        printf("Vi tri them khong hop le\n");
        return;
    }
    for(int j =i;j<*n+1;j++){
        arr[j] = arr[j-1];
    }
    arr[i] =them;
    (*n)++;
    printf("Da them phan tu %d o vi tri %d\n",them ,i);
}
int main (){
    int arr[100];
    int n,i,j,them;
    nhapmang(arr, &n);
    printf("Nhap vi tri can them: ");
    scanf("%d",&i);
    printf("Nhap gia tri can them: ");
    scanf("%d",&them);
    insertElement(arr,&n,i,them);
    for(int j =0;j<n;j++){
        printf("arr[%d] = %d\n",j,arr[j]);
    }
    return 0;
}