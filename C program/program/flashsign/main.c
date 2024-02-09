#include <stdio.h>
#include <stdlib.h>
int main()
{
    system("color 37");
    int row,col,n;
    printf("enter n:");
    scanf("%d",&n);
    for(row=1;row<=n;row++){
        for(col=1;col<=n;col++){
            if(row+col==n+1) printf("*");
            else printf(" ");
        }        printf("\n");
    }
     for(row=1;row<=1;row++){
        for(col=1;col<=n-n/2;col++){
            if(row==1) printf("* ");
        }        printf("\n");
    }
    for(row=1;row<=n;row++){
        for(col=1;col<=n;col++){
            if(row+col==n+1) printf("*");
            else printf(" ");
        }        printf("\n");
    }
    return 0;
}
