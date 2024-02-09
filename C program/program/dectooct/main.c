#include <stdio.h>
#include <stdlib.h>
int main()
{//dec to oct...
    system("color 37");
    int n, i=0;
    int oct_num[i];
    scanf("%d",&n);
    while(n>0){
        oct_num[i]=n%8;
        n/=8;
        i++;
    }
    for(int j=i-1;j>=0;j--)
    printf("%d",oct_num[j]);
    getch();
    return 0;
}
