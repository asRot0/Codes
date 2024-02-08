#include <stdio.h>
#include <stdlib.h>
int main()
{
    system("color 8F");
    int i,j,A[3][2],B[3][2],C[3][2];
    printf("values of array A:\n");
    for(i=0;i<3;i++)
        for(j=0;j<2;j++)
        scanf("%d",&A[i][j]);
    printf("values of array B:\n");
    for(i=0;i<3;i++)
        for(j=0;j<2;j++)
        scanf("%d",&B[i][j]);
     for(i=0;i<3;i++)
         for(j=0;j<2;j++)
            C[i][j]=A[i][j]+B[i][j];
    printf("values of array C:\n");
     for(i=0;i<3;i++)
         for(j=0;j<2;j++){
            printf("\t%d",C[i][j]);
            printf("\n");
            }
    getch();
    return 0;
}
//values of array A:5 10 15 20 25 30

//values of array B:35 40 45 50 55 60

//values of array C:40 50 60 70 80 90


