#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
void main()
{
    int i=0,j=0;
    int arr[3][3];
    int *ptr1;
    ptr1=&arr[0][0];
    printf("enter\n");
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++)
            scanf("%d",&arr[i][j]);
    }
    printf("following\n");
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            printf("%d ",*ptr1);
            ptr1++;
        }
        printf("\n");
    }
    getch();
}
