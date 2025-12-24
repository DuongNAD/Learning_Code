#include<stdio.h>

int main () {
	int n,i,j,k;
	int a[100];
	
	printf("Nhap so luong phan tu mang a: ");
	scanf("%d",&n);
	for(k =0;k<n;k++){
		printf("Nhap phan tu a[%d]: ",k); 
		scanf("%d",&a[k]);
	}
	for(i = 0; i< n-1;i++){
		for(j = i +1;j<n;j++){
			if(a[i]<a[j]){
				int temp = a[i];
				a[i] = a[j];
				a[j] = temp;
			}
		}
	}
	printf("Mang sap xep tu lon den be: ");
	for(i =0;i <n;i++){
		printf("%d\t ",a[i]);
	}
	
	return 0;
}