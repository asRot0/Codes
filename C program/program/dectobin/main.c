#include <stdio.h>
#include <stdlib.h>
int main()
{
    system("color 37");
    int n, i=0;
    int bin_num[i];
    scanf("%d",&n);
    while(n>0){
        bin_num[i]=n%2;
        n/=2;
        i++;
    }
    for(int j=i-1;j>=0;j--)
    printf("%d",bin_num[j]);
    getch();
    return 0;
}
