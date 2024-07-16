#include <stdio.h>
main()
{
    int n,f=1,m;
    printf("Enter the value of n:");
    scanf("%d",&n);
    for(m=1;m<=n;m++)
        f=f*m;
    printf("Factorial =%d",f);
    return 0;
}
