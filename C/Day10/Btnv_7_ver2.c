#include <stdio.h>
#include <string.h>

char *clearspace(char s[])
{
    char d[100];
    char *token = strtok(s, " ");
    while (token != NULL)
    {

        strcpy(d, token);
        token = strtok(NULL, " ");
        if(token != NULL){
            strcat (d," ");
        }
    }
}
int main()
{  
    char s[100];
    fgets(s,sizeof(s),stdin);
    char *d = clearspace(s);
    fputs(d,stdout);
    return 0;
}