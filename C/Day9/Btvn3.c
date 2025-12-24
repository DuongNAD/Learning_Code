#include<stdio.h>
#include<string.h>
int main () {
    char c[100];
    printf("Nhap chuoi: \n");
    fgets(c,sizeof(c),stdin);
    printf("Chuoi da nhap: \n");
    fputs (c,stdout);
    size_t size =strlen(c);
    if(size >0 && c[size - 1] == '\n'){
        c[size -1] == '\n';
        size--;
    }
    for(int i = strlen(c)-1;i>=0;i--){
        printf("%c",c[i]);
    }
    return 0;
}