#include<stdio.h>
#include<ctype.h>
int main () {
	int countV= 0, countD = 0, i, countS =0 ;
	char s[100];
	
	scanf("%[^\n]",s);
	
	for(i = 0;s[i] != '\0';i++){
		if(s[i] == 'A' || s[i] == 'a' || s[i] == 'E' || s[i] == 'e' || s[i] == 'I' || s[i] == 'i' || s[i] == 'O' ||s[i] == 'o' ||s[i] == 'U' || s[i] =='u' ){
			countV++;
		}
		else if(isdigit(s[i])){
			countD++;
		}
		else if(!isalnum(s[i]) && s[i] != ' '){
			countS++;
		}
		s[i] = toupper(s[i]);
	}
	
	printf("\nOUTPUT:\n");
	printf("%d\n",countV);
	printf("%d\n",countD);
	printf("%d\n",countS);
	printf("%s",s);
	return 0;
}