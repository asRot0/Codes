#include <stdio.h>
#include <stdlib.h>
int main()
{
    int a[2][2]={{5,4},{4,4}};
    int b[2][2]={{6,7},{4,6}};
    int s[2][2]={0};
    int i,j;
    for (i=0;i<2;i++)
        for(j=0;j<2;j++)
        s[i][j]=a[i][j]+b[i][j];
        printf("matrix a:\n");
    for (i=0;i<2;i++){
        for(j=0;j<2;j++)
            printf("%d\t",a[i][j]);
        printf("\n");
    }
    printf("\nmatrix b:\n");
        for (i=0;i<2;i++){
        for(j=0;j<2;j++)
            printf("%d\t",b[i][j]);
        printf("\n");
    }
    printf("\nsummation of two matrix s:\n");
        for (i=0;i<2;i++){
        for(j=0;j<2;j++)
            printf("%d\t",s[i][j]);
        printf("\n");
    }
    getch();
    return 0;
}
