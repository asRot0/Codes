#include <stdio.h>
#include <stdlib.h>
int main()
{
    system("color 37");
    int marks[4][10];
    int i,j;
    for(i=0;i<4;i++){
        for(j=0;j<10;j++){
            scanf("%d",&marks[i][j]);
        }
    }
    for(j=0;j<10;j++){
        marks[3][j]=marks[0][j]/4.0+marks[1][j]/4.0+marks[2][j]/2.0;
        printf("Roll No: %d\tTotal Marks: %d\n",j+1,marks[3][j]);
    }
    getch();
    return 0;
}
