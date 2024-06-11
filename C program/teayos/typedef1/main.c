#include <stdio.h>
#include <stdlib.h>
typedef signed char smallint;
int main(void)
{
    system("color 37");
    smallint i;
    for (i=0;i<10;i++)
        printf("%d ",i);
    return 0;
}
