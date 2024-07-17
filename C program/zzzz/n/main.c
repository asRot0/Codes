#include <stdio.h>
#include <stdlib.h>
int main()
{
    int i,n;
    float k=0;
    printf("input n:");
    scanf("%d",&n);
    for(i=1;i<=n;i++){
       k=k+(1/i);
    }
    printf("%f",k);
    return 0;
}
