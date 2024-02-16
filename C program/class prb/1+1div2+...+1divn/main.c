#include <stdio.h>
int main()
{
    int n;
    float s=0,i;
    printf("input n:");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
        s=s+1/i;
    printf("total=%.3f\n",s);
    getch();
    return 0;
}
