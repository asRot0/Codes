#include <stdio.h>
#include <stdlib.h>
int main()
{
    int a,b,mul=0,i;
    printf("en fas num:");
    scanf("%d",&a);
    printf("en sec num:");
    scanf("%d",&b);
    for(i=1;i<=b;i++)
        mul  += a;
    printf("%d",mul);
    return 0;
}
