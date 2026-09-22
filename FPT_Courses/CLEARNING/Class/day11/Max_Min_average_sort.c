#include<stdio.h>

int main () {
	int s[100];
	int n,i,j, ave = 0, sum = 0;
	
	scanf("%d",&n);
	for(i= 0;i<n;i++){
		scanf("%d",&s[i]);
		sum = sum +s[i];
	}
	
	ave = (float)sum/n;
	
	for( i = 0;i<n -1 ;i++){
		for(j = i+1 ;j<n;j++){
			if(s[i] <s[j]){
				int temp = s[i];
				s[i] = s[j];
				s[j] = temp;
			}
		}
	}
	printf("\nOUTPUT\n");
	printf("%d\n", s[n-1]);
	printf("%d\n",s[0]);
	printf("%d\n",ave);
	for(i = 0;i<n;i++){
		printf("%d\t", s[i]);
	}
}