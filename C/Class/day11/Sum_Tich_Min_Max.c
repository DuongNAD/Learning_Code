#include<stdio.h>


int main(){
	
	int n,i,min,max,sum=0,tich =1;
	int arr[100];
	for(i=0;i<n;i++){
		scanf("%d",arr[i]);
		sum = sum+arr[i];
		tich = tich*arr[i];
	}
	min = max = arr[0];
	for(i = 1;i<n;i++){
		if(min >arr[i]){
			min = arr[i];
		}
		else if(max < arr[i]){
			max = arr[i];
		}
	}	
	
	printf("\nOUTPUT:\n");
	printf("Tong: %d\n",sum);
	printf("Tich: %d\n",tich);
	printf("Min: %d\n",min);
	printf("Max: %d\n",max);
	
}