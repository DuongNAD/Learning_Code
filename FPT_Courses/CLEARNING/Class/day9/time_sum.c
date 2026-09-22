#include<stdio.h>
#include<time.h>
#include<stdlib.h>

int main () {
	long long sum = 0;
	clock_t start,end;
	
	start = clock();
	double time_used;
	for(int i =1;i<=100000000;i++){S
		sum = sum +1;
	}
	end = clock();
	time_used = ((double)(end-start))/CLOCKS_PER_SEC;
	
	printf("Time: %f seconds",time_used);
	return 0;
}