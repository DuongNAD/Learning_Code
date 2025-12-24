#include<stdio.h>

int sum(int n, int a[]){
	int tong =0;
	for(int  i= 0;i<n;i++){
		tong = tong +a[i];
	}
	return tong;
}

int sumNguyenAm(int n, char c){
	for(int i =0;i<n;i++){
		if(c[i] =='a' ||c[i] =='A'||c[i] ==)
	}
}

int main () {
	int n,i;
	int array[100];
	printf("Nhap so luong phan tu trong mang: ");
	scanf("%d",&n);
	for(i = 0;i<n;i++){
		printf("Nhap so %d: ",i+1);
		scanf("%d",&array[i]);
	}

	printf("\n");
	for(i = 0;i<n-1;i++){
		for(int j =i+1;j<n;j++){
			if(array[i] > array[j]){
			
			int temp = array[i];
			array[i] = ar	ray[j];
			array[j] = temp;
		}}
	}
	for(i = 0;i<n;i++){
		printf("%d\t",array[i]);
	}
	printf("\n");
	for(i = 0;i<n/2;i++){
		int temp =array[i];
		array[i] = array[n-i-1];
		array[n-1-i] = temp;
	}
	for(i = 0;i<n;i++){
		printf("%d\t",array[i]);
	}
	
	int Tong = sum(n,array);
	printf("Tong = %d",Tong);
	
	return 0;
}