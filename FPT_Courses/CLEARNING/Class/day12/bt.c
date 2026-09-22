#include<stdio.h>

float TaverageArray(int array[], int n){
	int i,sum =0;
	
	for(i =0;i<n;i++){
		sum = sum + array[i];
	}
	return sum/n;
}

void averageOddAboveMean(int array[], int n){
	int count = 0;
	int i, sum = 0;
	float tb = TaverageArray(array,n);
	for(i=0;i<n ;i++){
		if(array[i] %2 != 0 && array[i] >tb){
			sum = sum +array[i];
			count++;
		}
	}
	printf("%f",sum/count);
}

int main () {
	int array[100];
	int n,i;
	scanf("%d",&n);
	for(i = 0;i<n;i++){
		scanf("%d",&array[i]);
	}
	averageOddAboveMean(array,n);

	
	return 0;
}