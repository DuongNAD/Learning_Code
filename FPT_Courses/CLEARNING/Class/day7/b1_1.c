#include<stdio.h>
#include<time.h>
#include<stdlib.h>
int main () {
	int a,b,k;

	do {
		printf("Nhap a = ");
		scanf("%d",&a);
		printf("Nhap b (b>a) = ");
		scanf("%d",&b);
		if(a>=b){
			printf("\na phai >b");
		}
	}
	while(a>=b);
	
	printf("Nhap so nguyen k: ");
	scanf("%d",&k);
	
	srand(time(NULL));
	printf("Random: ");
	int i;
	for(i =0;i<k;i++){
		int randomNumber = rand() %(b-a +1) +a;
		printf("%d\t",randomNumber);
	}
	printf("\n");
	return 0;
	
}