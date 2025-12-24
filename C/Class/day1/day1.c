    #include<stdio.h>

    int main () {
        int a;
        printf("Nhap a = ");
        scanf("%d", &a);
        int c = 0;
        for (int i = a;i >0; i/2)
        {   
            a = a/2;
            if (a%2 ==1)
            {
                c = c*10 + 1;
            }
            else{
                continue;
            }
            
        }
        
        printf("%d",c);
        return 0;
        
    }