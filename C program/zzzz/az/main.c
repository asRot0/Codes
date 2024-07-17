#include <stdio.h>
int main()
{
    int i,j,n,px,py;
    n=4,px=n,py=n;
    for(i=1;i<n*2;i++){
        for(j=1;j<=n;j++){
            if(i==px||i==py)
                printf("*");
            else
                printf(" ");
        }
        px++;
        py--;
        printf("\n");
    }
    return 0;
}
