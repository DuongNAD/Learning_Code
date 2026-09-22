#include <stdio.h>
#include <string.h>

void str(){
    int x = 10;
    printf("Gia tri cua x: %d\n", x);
    printf("Dia chi cua x: %p\n", (void*)&x);
}
int main()
{
    int x=10;
    printf("Gia tri cua x: %d\n", x);
    printf("Dia chi cua x: %p\n", (void*)&x);

    str();
    char *c = "Hello World";
    printf("Hello World\n");
    printf("%d",strlen(c));
    
    return 0;
}