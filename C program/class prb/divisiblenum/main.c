#include <stdio.h>
#include <stdlib.h>
int main()
{
    int k;
    for(int i=100;i<200;i++){
        if(i%7==0){
        printf("%d\t",i);
      k=k+i;
        }
    }
    printf("\n%d",k);
    getch();
    return 0;
}
