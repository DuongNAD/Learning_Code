#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int main() {
  system("cls");
  //INPUT - @STUDENT:ADD YOUR CODE FOR INPUT HERE:
  
  int x,y;
  scanf("%d",&x);
  scanf("%d",&y);
  
  if(x>y){
  	return 0;
}
  int i;
  // Vòng lặp đếm số lượng số chẵn từ x tới y
  for(i = x; i<= y ; i++){
  	if(i%2==0){
  		i++;
	  }
  }
  int j;
  // Vòng lặp đếm số lượng số lẻ từ x tới y
  for(j = x; j<= y ; j++){
  	if(j%2!=0){
  	j++;
	  }
  }
  // Fixed Do not edit anything here.
  printf("\nOUTPUT:\n");
  //@STUDENT: WRITE YOUR OUTPUT HERE:
  
  printf("%d\n",i);
  printf("%d",j);
  
  
  
  //--FIXED PART - DO NOT EDIT ANY THINGS HERE
  printf("\n");
  system ("pause");
  return(0);
}
