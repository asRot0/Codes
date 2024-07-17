#include <stdio.h>
int main()
{
    int i,j,a,b;
    a=1;
    b=5;
    for(i=1;i<=2;i++){
        for(j=1;j<=5;j++){
            if(i==1)
                printf("%d",a++);
                if(i==2)
                printf("%d",b--);
                }
        printf("\n");
    }
    return 0;
}
