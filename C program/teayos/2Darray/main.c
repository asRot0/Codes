#include <stdio.h>
#include <stdlib.h>
int main()
{
    system("color F1");
    int twod[4][5];
    int i,j;
    for(i=0;i<4;i++)
        for(j=0;j<5;j++)
        twod[i][j]=i*j;
        printf("The program output looks like this::\n");
    for(i=0;i<4;i++){
        for(j=0;j<5;j++)
            printf("%d ",twod[i][j]);
        printf("\n");
    }
    return 0;
}
