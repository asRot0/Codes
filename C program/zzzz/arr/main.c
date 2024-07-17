#include <stdio.h>
#include <stdlib.h>
int main()
{
    system("color 37");
    int a[3][3]={{5,4,3},{4,4,4},{3,2,6}};
    int b[3][3]={{6,7,7},{4,3,8},{2,1,4}};
     int c[3][3]={0};
     int i,j,k;
     for(i=0;i<3;i++){
        for(j=0;j<3;j++){
        for(k=0;k<3;k++){
        c[i][j]=c[i][j]+a[i][k]*b[k][j];
        }
        }
        }
       for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            printf("%d\t",c[i][j]);
        }
        printf("\n");
}

    return 0;
}
