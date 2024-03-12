#include <stdio.h>
#include <stdlib.h>
int main()
{
    system("color F1");
    int row,col,n;
    printf("enter n:");
    scanf("%d",&n);
    for(row=1;row<=n;row++){
        for(col=1;col<=n;col++){
            if(row==col)
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }
    for(row=2;row<=n;row++){
        for(col=1;col<=n;col++){
            if(row+col==n+1)
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }
    getch();
    return 0;
}
