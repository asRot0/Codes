#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

int main()
{
    int i=0,c=0,x,a[30];
    printf("enter integer number:");
    scanf("%d",&x);
    while(x!=0){
        a[i++]=x%10;
        x=x/10;
        c++;
    }
    for(i=0;i<c;i++){
        for(int j=c-1-i;j>=0;j--){
            printf("%d\t",a[j]);
        }
        printf("\n");
    }
    getch();
}
