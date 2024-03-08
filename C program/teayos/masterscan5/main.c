#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int i,j;
    printf("enter a decimal number:");
    scanf("%d.%d",&i,&j);
    printf("left part: %d, right part: %d", i,j);
    return 0;
}
