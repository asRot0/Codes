#include<stdio.h>
#include<math.h>
main()
{
    int i,j,k,z,n;
    n=4,z=1;
    for(i=1;i<=n;i++){
        for(j=n-1;j>=i;j--){
            printf(" ");
        }
        for(k=z;k>=1;k--)
        {
            printf("%d",k);
        }
        z+=2;
        printf("\n");
    }
    return 0;
}
