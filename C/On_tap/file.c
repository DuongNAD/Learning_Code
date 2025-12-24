#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fptr;
    char filename= "data1.txt";
    char ch;
    fptr = fopen(filename, "r");
    if (fptr == NULL) {
        printf("The file is not opened. The program will"
		"now exit.");
		exit(0);
    }
    else{
    	printf("Open file ok !\n");
	}

    return 0; 
}