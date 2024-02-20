#include <stdio.h>
int main()
{
    int i,j,num=0;
    for(i=1;i<=9;i++){
       for(j=1;j<=i;j++){
        num--;
        printf("%d",num);
    }
      printf("\n");
    }
    return 0;
}
