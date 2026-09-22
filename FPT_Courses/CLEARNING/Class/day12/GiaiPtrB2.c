#include<stdio.h>
#include<math.h>

void ptrBac2 (float a, float b){
	float ktra = -b/a;
	if(ktra <0){
		printf("Ptr vo nghiem");
	}
	else if(ktra ==0){
		printf("x1 = x2 = 0");
	}
	else{
		printf("Ptr co 2 nghiem phan biet: \n");
		printf("x1 = %.2f\n",sqrt(ktra));
		printf("x2 = %.2f",-sqrt(ktra));
	}
}

int main () {
	float a,b;b
	scanf("%f",&a);
	scanf("%f",&b);
	if (a == 0) {
        if (b == 0) {
            printf("Ptr vo so nghiem (0x + 0 = 0)");
        } else {
            printf("Ptr vo nghiem (0x + b = 0 voi b != 0)");
        }
    } else {
    	printf("\nOUPUT\n")
	    ptrBac2(a, b);
    }
	return 0;
}