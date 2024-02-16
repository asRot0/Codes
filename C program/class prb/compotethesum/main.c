#include <stdio.h>
#include <stdlib.h>
int main()
{
    system("color 37");
    int sum,n;
    sum=0;
    printf("input n=");
    scanf("%d",&n);
    while(n>0){
        sum=sum+(n%10);
        n=n/10;
    }
    printf("Sum=%d",sum);
    getch();
    return 0;
}
