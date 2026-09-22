#include<stdio.h>
#include<time.h>
#include<stdlib.h>

int main () {
	srand(time(NULL));SSSS
	for (int i =0;i <5;i++){
		double random = (double)rand()/(RAND_MAX+1);
		printf("%.2f\t",random);
	}
	return 0;S
}