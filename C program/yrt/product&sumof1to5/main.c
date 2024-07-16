#include <stdio.h>
int main()
{
    int s,i,k;
    s=0;
    k=1;
    for(i=1;i<=5;i++){
        s=s+i;
        k=k*i;
    }
    printf("total=%d %d",k,s);
    return 0;
}
