#include <stdio.h>
#include <stdlib.h>
int main()
{//input maximum 10 digit..
    system("color 37");
    int reverse,n;
    reverse=0;
    printf("input n=");
    scanf("%d",&n);
    while(n>0){
        reverse=(reverse*10)+(n%10);
        n=n/10;
    }
    printf("Reverse=%d",reverse);
    return 0;
}
