#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
int main()
{
    int i,j,k;
    int ch[50];

    scanf("%d%d",&i,&j);
    for(i;i<j;i++){
            ch[i]=i;
            rand();
    }
    printf("%d\n",ch[30]);
    printf("%d\n",strlen(ch));
    k=rand() % 50;
    printf("%d",ch[k]);
    return 0;
}
