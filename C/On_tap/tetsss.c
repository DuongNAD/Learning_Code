#include <stdio.h>
#include <math.h>
int main (){
	printf("\nINPUT:\n");
    float height , width;
    scanf("%f",&height);
    scanf("%f",&width);
    
    float perimeter = ( height + width )*2;
    float area = height*width; 
	
	printf("\nOUTPUT:\n");
	
	printf("%.3f\n",perimeter);
	printf("%.3f",area);
	
	return 0;
}