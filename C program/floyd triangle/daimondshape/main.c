#include <stdio.h>
#include<math.h>
int main()
{
    int i,j,k;
    int n=3;
    for(i=n;i>=-n;i--){
        for(j=1;j<=abs(i);j++){
            printf(" ");
        }
        for(k=n;k>=abs(i);k---){
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}
