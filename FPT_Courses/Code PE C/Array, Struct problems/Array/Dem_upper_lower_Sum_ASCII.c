#include<stdio.h>

int main () {
	char s[100],i;
	int countU =0, countL =0, sum =0; 
	scanf("%[^\n]",s);
	
	for(i=0;s[i] != '\0';i++){
		if(s[i] >='A' && s[i] <='Z'){
			countU++;
		}
		else if(s[i] >= 'a' && s[i] <='z'){
			countL++;
		}
		
		sum = sum + s[i];
	}
	for(i =0;s[i] != '\0'; i++){
		if(isdigit(s[i])){
			s[i] = '#';
		}
	}
	
	printf("\nOUTPUT\n");
	printf("%d\n",countU);
	printf("%d\n",countL);
	printf("%d\n",sum);
	for(i = 0;s[i] != '\0';i++){
		printf("%c",s[i]);
	}
}