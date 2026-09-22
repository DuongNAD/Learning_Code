#include <stdio.h>
#include<string.h>
int main() {
    char s[100];
    int wc = 0 ,cc = 0,i;
    scanf("%[^\n]",s);
    int l = strlen(s);
    for(i = 0;i<l;i++){
    	if(s[i] != ' '){
    		cc++;
		}
		
		if(s[i] != ' ' && (s[i-1] == ' ' || i == 0)){
			wc++;
		}
	}
	
	printf("%d\n",cc);
	printf("%d",wc);
    return 0;
}