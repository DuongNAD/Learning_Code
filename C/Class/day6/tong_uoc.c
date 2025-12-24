#include<stdio.h>

 int sum_uoc ( int n){
 	int i;
 	int sum;
 	for(i =1;i<=n;i++){
 		if (n%i == 0){
 			sum = sum +i;
		 }
	 }
	 return sum;
 }

int main () {
	int n;
	printf("n = ");
	scanf("%d",&n);
	printf("%d",sum_uoc(n));
	return 0;
}