#include <stdio.h>
int main()
{
    int k,s=0;
    for(k=1;k<=50;k++)
        if(k%2==0)
        s=s+k;
    printf("total is=%d",s);
    return 0;
}
