#include <stdio.h>
int main()//largest number...
{
    int  a,b,c;
    printf("Enter three numbers a,b,c :");
    scanf("%d%d%d",&a,&b,&c);
    if(a>b){
            if(a>c)
                printf("\t%d is the largest number.",a);
        else
                printf("\t%d is the largest number.",c);
      }
    else{
        if(b>c)
            printf("\t%d is the largest number.",b);
        else
            printf("\t%d is the largest number.",c);
    }
getch();
}
