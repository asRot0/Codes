#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i,n,arr1[n];
    scanf("%d",&n);
    for(i=0;i<n;i++){
        scanf("%d",&arr1[i]);
    }
    for(i=n-1;i>0;i--){
        printf("%d",arr1[i]);
    }
    return 0;
}
