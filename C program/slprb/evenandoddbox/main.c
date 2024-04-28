#include <stdio.h>
int main()
{
    int i,j,a,b;
    a=-2;
    b=-1;
    for(i=1;i<=2;i++){
        for(j=1;j<=5;j++){
            if(i==1)
                printf("%d ",a+=2);
            if(i==2)
                printf("%d ",b+=2);
            }
            {
            if(i==1&&j==6)
                printf("\teven numbers.");
            if(i==2&&j==6)
                printf("\todd numbers.");
                }
        printf("\n");
    }
    printf("\afrom (0 to 9)...");
    return 0;
}
