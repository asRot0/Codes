#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int i,j;
    printf("enter an integer:"); //enter the number 12345, i will be assigned 123, and j will have the value 45.
    scanf("%3d%d",&i,&j);
    printf("i=%d\nj=%d",i,j);
    return 0;
}
