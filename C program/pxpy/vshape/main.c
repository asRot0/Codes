#include <stdio.h>
int main()
{
    int i,j;
    int n=5,px=1,py=n*2-1;
    for(i=1;i<=n;i++){
        for(j=1;j<n*2;j++){
            if(j==px||j==py)
                printf("*");
            else
                printf(" ");
        }
        px++;
        py--;
        printf("\n");
    }
    getch();
    return 0;
}
