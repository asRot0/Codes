#include <stdio.h>
#include <stdlib.h>
int main()
{
    system("color F1");
    int marks[4][10];
    int i,j;
    printf("Total mark =(25%% of 1st terminal + 25%% of 2nd terminal + 50%% of final exam).......\n\n");
    for(i=0;i<4;i++){
        if(i==0) printf("First terminal exam:");
        if(i==1) printf("Second terminal exam:");
        if(i==2) printf("Final exam:");
        if(i==3) printf("Total marks:");
        for(j=0;j<10;j++){
            scanf("%d",&marks[i][j]);
        }
    }
    printf("\n");
    for(j=0;j<10;j++){
        marks[3][j]=marks[0][j]/4.0+marks[1][j]/4.0+marks[2][j]/2.0;
        printf("Roll No: %d\tTotal Marks: %d\n",j+1,marks[3][j]);
    }
    getch();
    return 0;
}
//Roll: 1,2,3,4,5,6,7,8,9,10::
//std first terminal exam marks 80 70 92 78 58 83 85 66 99 81::
//std second terminal exam marks 75 67 55 100 91 84 79 61 90 97::
//std final exam marks 98 67 75 89 81 83 80 90 88 77::
//total marks 0 0 0 0 0 0 0 0 0 0::
