#include<stdio.h>
#include<ctype.h>
#include<string.h>
int main () {
	int countU =0, countL=0,i;
	char s[100];
	scanf("%[^\n]",s);
	for(i=0;s[i] != '\0';i++){
		if(s[i] >='A' &&s[i] <= 'Z'){
			countU++;
		}
		else if(s[i] >='a' &&s[i] <= 'z'){
			countL++;
		}
	}
	int l = strlen(s);
	
	printf("\nOUTPUT:\n");
	printf("%d\n",countU);
	printf("%d\n",countL);
	printf("%d\n",s[0] - s[l-1]);
	for(i=0;s[i] != '\0';i++){
		s[i] = tolower(s[i]);
	}
	printf("%s",s);
	return 0;
}