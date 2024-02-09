#include <stdio.h>
#include<stdlib.h>
int main()
{
    system("color 37");
    int i,j,n;
    printf("enter n:");
    scanf("%d",&n);
    for(i=8;i>=n;i--){
       for(j=n;j<=8;j++){
        printf("%d  ",j);
       }
          n+=1;
       printf("\n");

    }
    return 0;
}
