#include<stdio.h>

int main () {
    FILE *file = fopen("bt1","a");
    if(file == NULL){
        printf("Error\n");
    }
    else {
        printf("Ghi file thanh cong\n");
    }
    fprintf(file,"Nice to meet you\n");
    fclose(file);
    return 0;
}