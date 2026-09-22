#include<stdio.h>

int main () {
	int n,i;
	float arr[100];
	int countPass =0, countFail=0;
	scanf("%d",&n);
	for( i =0; i<n;i++){
		scanf("%f",&arr[i]);
		if(arr[i] >=5 ){
			countPass++;
		}
		
		else{
			countFail++;
		}
	}
	float min = arr[0];
	float max = arr[0];
	for(i = 1;i<n;i++){
		if(min >arr[i]){
			min = arr[i];
		}
		else if(max <arr[i]){
			max = arr[i];
		}
	}
	printf("\nOUTPUT\n");
	printf("%d",countPass);
	printf("%d",countFail);
	printf("%f",max);
	printf("%f",min);
}