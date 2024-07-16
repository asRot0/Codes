#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i,n;
    printf("how many elements??__");
    scanf("%d",&n);
    int arr1[n];
    for(i=0;i<n;i++){
            printf("element no:%d=",i+1);
        scanf("%d",&arr1[i]);
    }
    printf("reverse order:");
    for(i=n-1;i>=0;i--){
        printf("%d",arr1[i]);
    }
    getch();
    return 0;
}
