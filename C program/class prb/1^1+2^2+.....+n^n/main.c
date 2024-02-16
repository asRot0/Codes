#include <stdio.h>
#include <math.h>
int main()
{
    int s=0,i,p,n;
    printf("Enter the value n:");
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        p=pow(i,i);
        s=s+p;
    }
    printf("total=%d",s);
    return 0;
}
